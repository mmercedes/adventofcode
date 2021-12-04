;; to run this file `emacs --script day_03.el`

;;;;;; part 1

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

(defun sum_binary_lines (lines)
  "given lines of 101,001,111 return (2 1 3)" 
  (setq line_len 0)
  (setq char_count_list nil)
  (dolist (line lines)
    (when (eq line_len 0)
      ;; initalize vars on first loop
      (setq line_len (length line))
      (setq char_count_list (make-list line_len 0)))
    (setq char_count_list
          ;; add value of each char in line to char_count_list.
          ;; index of char_count_list represents sum of
          ;; values of each line at that index
          (mapcar* #'+
                  char_count_list
                  ;; convert string line "100110" -> (1 0 0 1 1 0)
                  (mapcar 'string-to-number (mapcar 'char-to-string line))))))

(defun part1 ()
  "compute gamma rate * epsilon rate"
  (setq gamma "")
  (setq epsilon "")
  (setq lines (read_file_to_alist "./inputs/input_03.txt"))
  (setq half (/ (length lines) 2))
  (sum_binary_lines lines)
  (dolist (i char_count_list)
    (setq gamma (concat gamma (if (> i half) "1" "0")))
    (setq epsilon (concat epsilon (if (<= i half) "1" "0"))))
  (* (string-to-number gamma 2) (string-to-number epsilon 2)))

(princ (format "part 1 answer: %i\n" (part1)))

;;;;;; part 2

;; uses global var char_count_list from p1

(defun part2 ()
  ""
  ;; reuse lines var from p1
  ;; calculate oxygen rating then reread lines later
  (setq gamma_index 1)
  (princ (format "gamma: %s epsilon: %s\n" gamma epsilon))

  ;; assumes there will be one left before gamma_mask overruns length of gamma string
  (while (> (length lines) 1)
    (dotimes (i (length lines))
      (setq current_line (pop lines))
      (setq gamma_mask (substring gamma 0 gamma_index))
      (when (string-prefix-p gamma_mask current_line)
        (add-to-list 'lines current_line t)))
    (setq gamma_index (+ gamma_index 1)))
  (setq oxygen_rating (pop lines))
  
  ;; same logic as above, but with epsilon mask
  (setq lines (read_file_to_alist "./inputs/input_03.txt"))
  (setq epsilon_index 1)
  
  (while (> (length lines) 1)
    (dotimes (j (length lines))
      (setq current_line (pop lines))
      (setq epsilon_mask (substring epsilon 0 epsilon_index))
      (when (string-prefix-p epsilon_mask current_line)
        (add-to-list 'lines current_line t)))
    (setq epsilon_index (+ epsilon_index 1)))
  (setq co2_rating (pop lines))
  
  (princ (format "oxygen_rating: %s co2_rating %s\n" oxygen_rating co2_rating))
  (* (string-to-number oxygen_rating 2)
     (string-to-number co2_rating 2)))
    
(princ (format "part 2 answer: %i\n" (part2)))
