;; to run this file `emacs --script day_02.el`

;;;;;; part 1

(defun read_file_to_alist (file)
  "read file into string"
  (split-string (with-temp-buffer
                  (insert-file-contents file)
                  (buffer-string))
                "\n" t))

(defun get_coords_from_cmd (cmd h d)
  "parse cmd string into new coordinates"
  (setq direction (nth 0 (split-string cmd " ")))
  (setq value (string-to-number (nth 1 (split-string cmd " "))))
  (cond ((string-equal "forward" direction) (list (+ h value) d))
        ((string-equal "up" direction)      (list h (- d value)))
        ((string-equal "down" direction)    (list h (+ d value)))))

(defun part1 ()
  "apply commands to coords and ret horizontal*depth"
  (setq horizontal 0)
  (setq depth 0)
  (dolist (line (read_file_to_alist "./inputs/input_02.txt"))
    (setq coords (get_coords_from_cmd line horizontal depth))
    (setq horizontal (pop coords))
    (setq depth (pop coords)))
  (* horizontal depth))

(princ (format "part 1 answer: %i\n" (part1)))

;;;;;; part 2

(defun get_coords_from_cmd_p2 (cmd h d a)
  "parse cmd string into new coordinates"
  (setq direction (nth 0 (split-string cmd " ")))
  (setq value (string-to-number (nth 1 (split-string cmd " "))))
  (cond ((string-equal "forward" direction) (list (+ h value) (+ d (* a value)) a))
        ((string-equal "up" direction)      (list h d (- a value)))
        ((string-equal "down" direction)    (list h d (+ a value)))))
        
(defun part2 ()
  "apply commands to coords and ret horizontal*depth"
  (setq horizontal 0)
  (setq depth 0)
  (setq aim 0)
  (dolist (line (read_file_to_alist "./inputs/input_02.txt"))
    (setq coords (get_coords_from_cmd_p2 line horizontal depth aim))
    (setq horizontal (pop coords))
    (setq depth (pop coords))
    (setq aim (pop coords)))
  (* horizontal depth))

(princ (format "part 2 answer: %i\n" (part2)))
