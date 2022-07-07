(define (over-or-under num1 num2) 
    (if (< num1 num2) (print -1))
    (if (= num1 num2) (print 0))
    (if (> num1 num2) (print 1))
)

(define (over-or-under num1 num2) 
    (cond
    ((< num1 num2) (print -1))
    ((= num1 num2) (print 0))
    ((> num1 num2) (print 1))
    )
)

(define (make-adder num) 
    (lambda (inc) (+ num inc))
)

(define (composed f g) 
    (lambda (x) (f (g x) ) )
)

(define lst 
    (list (list 1 nil) 
          2 (list 3 4)
          5)
)

(define lst 
    (cons (cons 1 nil) (cons 2 (cons 3 (cons 4 nil)) (cons 5 nil))
    )
)

(define (remove item lst)
  (cond ( (null? lst) '() )             ; base case
        ( (= item (car lst)) (remove item (cdr lst)))           ; exclude item
        ( else (cons (car lst) (remove item (cdr lst)))))       ; include item
)
