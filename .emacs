(package-initialize)

(define-key global-map (kbd "RET") 'newline)
(add-hook 'html-mode-hook '(lambda ()
                             (local-set-key (kbd "RET") 'newline)))
(setq backup-directory-alist '(("" . "~/.emacs.d/emacs-backup")))
(add-to-list 'load-path "~/org/.emacs.d/")
(require 'web-mode)
(require 'highlight-chars)
(add-hook 'font-lock-mode-hook 'hc-highlight-tabs)
(add-to-list 'auto-mode-alist'("\\.js\\'" . javascript-mode))
(add-to-list 'auto-mode-alist '("\\.jscad\\'" . javascript-mode))
(add-to-list 'auto-mode-alist '("\\.json\\'" . javascript-mode))
(add-to-list 'auto-mode-alist '("\\.jsx\\'" . web-mode))
(autoload 'javascript-mode "javascript" nil t)
(add-to-list 'auto-mode-alist '("\\.less\\'" . css-mode))
(add-to-list 'auto-mode-alist '("\\.scss\\'" . css-mode))
(add-to-list 'auto-mode-alist '("\\.md\\'" . rst-mode))
(add-to-list 'auto-mode-alist '("\\.tag\\'" . html-mode))
(add-to-list 'auto-mode-alist '("\\.tpl\\'" . html-mode))
(require 'org-install)
(add-to-list 'auto-mode-alist '("\\.org$" . org-mode))
(define-key global-map "\C-cl" 'org-store-link)
(define-key global-map "\C-ca" 'org-agenda)
(setq org-log-done t)
(setq org-agenda-files (list "~/org/"))
(setq org-agenda-files (list "~/org/memcached.org"
                             "~/org/pipedreams.org"
                             "~/Dropbox/org/"))

; export INDENT=number to set global value for indent
; export INDENT=number to set global value for indent
(setq myindent 2)
(if (getenv "INDENT")
    (setq myindent (string-to-number (getenv "INDENT")))
    (setq myindent myindent))

(setq css-indent-offset myindent)
(setq js-indent-level myindent)
(setq javascript-indent-level myindent)

(setq-default python-indent myindent) ;emacs 23
(setq-default python-indent-offset myindent); emacs 24
(add-hook 'python-mode-hook
    (lambda () (setq tab-width myindent)))
(setq html-indent-offset myindent)
(setq-default indent-tabs-mode nil)
(setq default-tab-width myindent)
(add-hook 'html-mode-hook
      (lambda()
      (setq sgml-basic-offset myindent)))

; JSX for react
;(add-to-list 'load-path "~/.emacs.d/site-lisp/")
;(add-to-list 'auto-mode-alist '("\\.jsx\\'" . jsx-mode))
;(autoload 'jsx-mode "jsx-mode" "JSX mode" t)

;jade and coffee
;(require 'jade-mode)    
;(add-to-list 'auto-mode-alist '("\\.jade$" . jade-mode))

;php
;(autoload 'php-mode "php-mode" "Major mode for editing php code." t)
;(add-to-list 'auto-mode-alist '("\\.php$" . php-mode))
;(add-to-list 'auto-mode-alist '("\\.inc$" . php-mode))

;blackspot specific
;(defun blackspot-after-save-hook ()
;  "After saving a less file, run the language_update file"
;  (if buffer-file-name
;      (progn
;        (setq is-less-file (numberp (string-match "blackspotnyc.com.+\.less$" buffer-file-name)))
;        (if is-less-file
;            (progn
;              (setq cmd (concat (getenv "B") "/home/felixc/less_and_compress.sh "))
;              (shell-command (concat cmd buffer-file-name))
;              (message "Updated .css, -min.css with %s" buffer-file-name))))))
;(add-hook 'after-save-hook 'blackspot-after-save-hook)

;Octave
(autoload 'octave-mode "octave-mod" nil t)
(setq auto-mode-alist
      (cons '("\\.m$" . octave-mode) auto-mode-alist))
