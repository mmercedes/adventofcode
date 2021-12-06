(require 'cl-lib)

(defun mapcar* (f &rest xs)
  "MAPCAR for multiple sequences"
  (if (not (memq nil xs))
      (cons (apply f (mapcar 'car xs))
            (apply 'mapcar* f (mapcar 'cdr xs)))))

(defun read_file_to_alist (file)
  "read file into string"
  (split-string (with-temp-buffer
                  (insert-file-contents file)
                  (buffer-string))
                "\n" t))

(defun parse_boards ()
  "read input into bingo boards var"
  (setq lines (read_file_to_alist "./inputs/input_04.txt"))
  (setq moves (mapcar 'string-to-number (split-string (pop lines) ",")))
  (setq boards (list))
  (setq current-board (list))
  (dotimes (i (length lines))
    (setq current-line (pop lines))
    ;; every 6th line is a space between boards
    (if (eq 0 (mod i 6))
        (when (not (eq 0 i))
          (push current-board boards)
          (setq current-board (list)))
      ;; convert "1 2 34" -> ("1" "2" "34")
      ;; and append to current-board
      (push (mapcar 'string-to-number (delete "" (split-string current-line))) current-board)))
  )

(defun make_move (move)
  "mark off the number move on all boards"
  (dolist (board boards)
    (dolist (row board)
      ;; if the row contains the called number
      (when (cl-position move row)
        ;; overrite the number with -1 to signify a hit
        (setcar (nthcdr (cl-position move row) row) -1)))))

(defun sum_board (board)
  (setq winner_board_sum 0)
  (dolist (row board)
    (dolist (i row)
      (when (not (eq -1 i)) (setq winner_board_sum (+ winner_board_sum i))))))

;; use cl-defun so there can be an arbitrary return point
(cl-defun is_winner ()
  "check if any board has bingo and set var for sum of all unmarked numbers if so"
  (setq winner_board_sum -1)
  ;; assume boards are 5x5 so a hit is 5 * -1
  (setq board_hit_num -5)
  (dolist (board boards)
    ;; check for horizontal bingo
    (dolist (row board)
      ;; if all values in a row are -1 their sum will equal board_hit_num
      (when (equal board_hit_num (apply '+ row))
        (sum_board board)
        (cl-return-from is_winner)))
    ;; check for vertical bingo
    ;; list representing the sums of each vertical cols
    (setq vert_sums '(0 0 0 0 0))
    (princ "board:\n")
    (dolist (row board) (princ (format "%s\n" row)) (setq vert_sums (mapcar* #'+ vert_sums row)))
    (princ (format "\nsums: %s\n" vert_sums))
    (dolist (sum vert_sums)
      (when (equal board_hit_num sum)
        (sum_board board)
        (cl-return-from is_winner)))))
        
(cl-defun part1 ()
  ""
  (setq part1_ans nil)
  (parse_boards)
  (dolist (m moves)
    (make_move m)
    (is_winner)
    (when (> winner_board_sum -1)
      (princ (format "ws: %i m:%i \n" winner_board_sum m))
      (setq part1_ans (* m winner_board_sum))
      (cl-return-from part1))))

;;(parse_boards)
;;(setq exb (pop boards))
;;(sum_board exb)
;;(princ (format "sum of board: %i\nboard %s\n" winner_board_sum exb))
(part1)
(princ (format "part 1 ans: %s\n" part1_ans))
