(add-to-list 'auto-mode-alist '("\\.js\\'" . javascript-mode))
(add-to-list 'auto-mode-alist '("\\.json\\'" . javascript-mode))
(autoload 'javascript-mode "javascript" nil t)
(add-to-list 'auto-mode-alist '("\\.less\\'" . css-mode))
(add-to-list 'auto-mode-alist '("\\.md\\'" . rst-mode))
(require 'org-install)
(add-to-list 'auto-mode-alist '("\\.org$" . org-mode))
(define-key global-map "\C-cl" 'org-store-link)
(define-key global-map "\C-ca" 'org-agenda)
(setq org-log-done t)
(setq org-agenda-files (list "~/org/"))
(setq org-agenda-files (list "~/org/memcached.org"
                             "~/org/pipedreams.org"
                             "~/Dropbox/org/"))
(custom-set-variables
  ;; custom-set-variables was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 '(org-agenda-files (quote ("/home/chriscauley/Dropbox/org/apps.org" "/home/chriscauley/Dropbox/org/articles.org" "/home/chriscauley/Dropbox/org/baseVB.org" "/home/chriscauley/Dropbox/org/books.org" "/home/chriscauley/Dropbox/org/change_of_address.org" "/home/chriscauley/Dropbox/org/cm_meeting.org" "/home/chriscauley/Dropbox/org/haiku.org" "/home/chriscauley/Dropbox/org/howto.org" "/home/chriscauley/Dropbox/org/memcached.org" "/home/chriscauley/Dropbox/org/modules.org" "/home/chriscauley/Dropbox/org/pipedreams.org" "/home/chriscauley/Dropbox/org/plusone.org" "/home/chriscauley/Dropbox/org/syncwell.org" "/home/chriscauley/Dropbox/org/tag.org" "/home/chriscauley/Dropbox/org/team.org" "/home/chriscauley/Dropbox/org/todo.org" "/home/chriscauley/Dropbox/org/weekly.org" "/home/chriscauley/Dropbox/org/work.org"))))
(custom-set-faces
  ;; custom-set-faces was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 )
(setq css-indent-offset 2)
(setq js-indent-level 2)
(setq javascript-indent-level 2)
(setq-default python-indent 4)
(setq html-indent-offset 2)
(add-hook 'html-mode-hook
	            (lambda()
		                  (setq sgml-basic-offset 2)
				              (setq indent-tabs-mode nil)))