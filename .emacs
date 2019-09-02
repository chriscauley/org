(require 'package)
(add-to-list 'package-archives
             '("marmalade" . "http://marmalade-repo.org/packages/") t)
(add-to-list 'package-archives
             '("melpa" . "http://melpa.milkbox.net/packages/") t)
(add-to-list 'package-archives
             '("melpa-stable" . "https://stable.melpa.org/packages/") t)

(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

(add-to-list 'load-path "~/org/.emacs.d/")

;; remove auto-newline because many projects don't have it
(setq require-final-newline nil)
(setq mode-require-final-newline nil)

;; nuke auto indent because I don't play like that
(electric-indent-mode -1)

;; show all tabs
(require 'highlight-chars)
(add-hook 'font-lock-mode-hook 'hc-highlight-tabs)

;highlight trailing whitespace
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (rjsx-mode slim-mode coffee-mode)))
 '(show-trailing-whitespace t))

; unsure if this is still relevant, I think electric-indent-mode covers it
;(define-key global-map (kbd "RET") 'newline)
;(add-hook 'html-mode-hook '(lambda ()
;                             (local-set-key (kbd "RET") 'newline)))

; get the *~ files out of sight
(setq backup-directory-alist '(("" . "~/.emacs.d/emacs-backup")))

(setq auto-save-visited-interval 300)

(require 'web-mode)
;(add-to-list 'auto-mode-alist'("\\.js\\'" . rjsx-mode))
(add-to-list 'auto-mode-alist '("\\.jscad\\'" . rjsx-mode))
(add-to-list 'auto-mode-alist '("\\.json\\'" . rjsx-mode))
(add-to-list 'auto-mode-alist '("\\.jsx\\'" . rjsx-mode))
(add-to-list 'auto-mode-alist '("\\.tag\\'" . html-mode))
(add-to-list 'auto-mode-alist '("\\.html\\'" . html-mode))
(setq js2-strict-missing-semi-warning nil)
(add-to-list 'auto-mode-alist '("\\.less\\'" . css-mode))
(add-to-list 'auto-mode-alist '("\\.scss\\'" . css-mode))
(add-to-list 'auto-mode-alist '("\\.md\\'" . rst-mode))
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
(setq my-width 2)
(setq-default default-tab-width 2)
(if (getenv "INDENT")
    (setq my-width (string-to-number (getenv "INDENT")))
    (setq tab-width my-width)
    (setq default-tab-width 2)
    )

(setq css-indent-offset my-width)
(setq js-indent-level my-width)
(setq javascript-indent-level my-width)

(setq-default python-indent-offset my-width);
(add-hook 'python-mode-hook
    (lambda () (setq tab-width my-width)))
(setq html-indent-offset my-width)
(setq-default indent-tabs-mode nil)
(setq default-tab-width my-width)
(add-hook 'rjsx-mode-hook (lambda()(setq tab-width my-width)))
(add-hook 'js-mode-hook (lambda()(setq tab-width my-width)))
(add-hook 'javascript-mode-hook (lambda()(setq tab-width my-width)))
(add-hook 'html-mode-hook (lambda()(setq tab-width my-width)))

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

;no magic comment in ruby mode
(setq ruby-insert-encoding-magic-comment nil)

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
 ;; custom-set-faces was added by Custom.

;;; Provide vimmy escape hatch to `evil-mode'.  Press ⌘-/ or M-⌘-/ to
;;; toggle `evil-mode'.
(global-set-key (kbd "s-/") 'evil-mode)
(global-set-key (kbd "M-/") 'evil-mode)
(global-set-key (kbd "M-s-/") 'evil-mode)
(global-set-key (kbd "M-SPC") 'set-mark-command)

(defun xah-comment-dwim ()
  "Like `comment-dwim', but toggle comment if cursor is not at end of line.

URL `http://ergoemacs.org/emacs/emacs_toggle_comment_by_line.html'
Version 2016-10-25"
  (interactive)
  (if (region-active-p)
      (comment-dwim nil)
    (let (($lbp (line-beginning-position))
          ($lep (line-end-position)))
      (if (eq $lbp $lep)
          (progn
            (comment-dwim nil))
        (if (eq (point) $lep)
            (progn
              (comment-dwim nil))
          (progn
            (comment-or-uncomment-region $lbp $lep)
            ))))))

(global-set-key (kbd "M-;") 'xah-comment-dwim)
(setq column-number-mode t)
