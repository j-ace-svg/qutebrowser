config.load_autoconfig()
normal_editor_command = "['gnome-terminal', '--wait', '--', 'nvim', '{file}', '-c', 'normal {line}G{column0}G']"
text_editor_command = "['gnome-terminal', '--wait', '--', 'nvim', '{file}', '-u', '~/.config/qutebrowser/textbox-nvim-config.vim', '-c', 'normal {line}G{column0}G']"
c.editor.command = ['gnome-terminal', '--wait', '--', 'nvim', '{file}', '-u', '~/.config/qutebrowser/textbox-nvim-config.vim', '-c', 'normal {line}G{column0}G']
#c.editor.command = ['gnome-terminal', '--wait', '--', 'nvim', '{file}', '-c', 'normal {line}G{column0}G']
#c.editor.command = ['nvim', '{file}', '-c', 'normal {line}G{column0}G']
#c.editor.command = ['gedit', '{file}', '+{line}:{column}']

#######################
# Boilerplate
#######################

bind = config.bind
unbind = config.unbind

# Unbind space
bind('<Space><Space>', 'nop')
bind('<Shift+Space>', 'nop')

#######################
# Settings
#######################

# Search engines
c.url.searchengines['DEFAULT'] = 'https://duckduckgo.com/?q={}'
c.url.searchengines['yt'] = 'https://www.youtube.com/results?search_query={}'
c.url.searchengines['gh'] = 'https://github.com/search?q={}'
c.url.searchengines['gp'] = 'https://github.com/search?q={}+user%3Aj-ace-svg'
c.url.searchengines['wr'] = 'https://www.wordreference.com/es/translation.asp?tranword={}'
c.url.searchengines['sd'] = 'https://www.spanishdict.com/translate/{}'
c.url.searchengines['sm'] = 'https://mail.google.com/mail/u/1/#search/{}'

#######################
# Normal Mode
#######################

# Enter command line mode
bind('<Space>;', 'set-cmd-text :')
bind('<Space>h', 'set-cmd-text -s :help -t')

# Vim like 'o' behavior
c.aliases['Open'] = 'spawn --userscript Open.sh'
c.aliases['Prepend'] = 'spawn --userscript Prepend.sh'
bind('o', 'set-cmd-text -s :open -t -r')
bind('O', 'set-cmd-text -s :Open')
bind('I', 'set-cmd-text -s :Prepend')
bind('A', 'set-cmd-text -s :open -t')
bind('e', 'set-cmd-text -s :open')

# Edit config
bind('se', f'set editor.command "{normal_editor_command}" ;; config-edit ;;  later 10 set editor.command "{text_editor_command}"')
bind('so', 'config-source')

# Movement
bind('<Ctrl-h>', 'fake-key <Ctrl-left>')
bind('<Ctrl-l>', 'fake-key <Ctrl-right>')
bind('<Ctrl-t>', 'fake-key <Enter>')
bind('gh', ':scroll-to-perc --horizontal 0')
bind('gl', ':scroll-to-perc --horizontal 100')

# Interact with page
bind(';', 'mode-enter normal', mode='hint')
bind('<Space>', 'mode-enter normal', mode='hint')
bind(';c', 'hint all right-click')
bind(';s', 'hint --rapid')
bind(';l', 'hint links')
bind(';L', 'hint links tab-bg')
bind('<Space>l', 'hint links tab-fg')
bind('<Space>f', 'hint all tab-fg')
bind(';e', 'hint inputs run edit-text')
bind('ge', f'set editor.command "{text_editor_command}" ;; edit-text ;; later 10 set editor.command "{normal_editor_command}"')
bind('<Space>/', 'search')

# Tabs
bind('gj', 'tab-focus -1')
bind('gk', 'tab-focus 1')

# Bitwarden
bind('<Space>pf', 'spawn --userscript qute-bitwarden')
bind('<Space>pu', 'spawn --userscript qute-bitwarden --username-only')
bind('<Space>pp', 'spawn --userscript qute-bitwarden --password-only')

# MPV
bind('<Space>mf', 'hint links spawn --detach mpv --force-window yes {hint-url} script-opts=ytdl_hook-ytdl_path=yt-dlp,ytdl_hook-try_ytdl_first=yes,ytdl_hook-exclude="%.webm$|%.ts$|%.mp3$|%.m3u8$|%.m3u$|%.mkv$|%.mp4$|%.VOB$" --fullscreen')
bind('<Space>mm', 'spawn --detach mpv --force-window yes {url} script-opts=ytdl_hook-ytdl_path=yt-dlp,ytdl_hook-try_ytdl_first=yes,ytdl_hook-exclude="%.webm$|%.ts$|%.mp3$|%.m3u8$|%.m3u$|%.mkv$|%.mp4$|%.VOB$" --fullscreen')
bind('<Space>mg', 'hint images spawn --detach mpv --force-window yes {hint-url} script-opts=ytdl_hook-ytdl_path=yt-dlp,ytdl_hook-try_ytdl_first=yes,ytdl_hook-exclude="%.webm$|%.ts$|%.mp3$|%.m3u8$|%.m3u$|%.mkv$|%.mp4$|%.VOB$" --fullscreen')

# Adjust browser chrome
bind('xb', 'config-cycle statusbar.show always in-mode')
bind('xt', 'config-cycle tabs.show always never')
bind('xx', 'config-cycle statusbar.show always in-mode;; config-cycle tabs.show always never')

# Dvorak hints
bind('xd', 'config-cycle hints.chars "asdfghjkl" "aoeuidhtns" ;; set hints.chars')

#######################
# Insert Mode
#######################

# Exit insert mode
bind('jk', 'mode-enter normal', mode='insert')
bind('kj', 'mode-enter normal', mode='insert')
#bind('<Escape>', 'fake-key <Escape>', mode='insert')

# Readline bindings
bind('<Ctrl-a>', 'fake-key <Home>', mode='insert')
bind('<Ctrl-e>', 'fake-key <End>', mode='insert')
bind('<Ctrl-b>', 'fake-key <Left>', mode='insert')
bind('<Ctrl-Shift-b>', 'fake-key <Ctrl-Left>', mode='insert')
bind('<Ctrl-f>', 'fake-key <Right>', mode='insert')
bind('<Ctrl-Shift-f>', 'fake-key <Ctrl-Right>', mode='insert')
bind('<Ctrl-j>', 'fake-key <Enter>', mode='insert')
bind('<Ctrl-t>', 'fake-key <Enter>', mode='insert')
bind('<Ctrl-h>', 'fake-key <Backspace>', mode='insert')
bind('<Ctrl-w>', 'fake-key <Ctrl-Backspace>', mode='insert')
bind('<Ctrl-d>', 'fake-key <Delete>', mode='insert')
bind('<Ctrl-Shift-d>', 'fake-key <Ctrl-Delete>', mode='insert')
bind('<Ctrl-i>', 'fake-key <Tab>', mode='insert')
bind('<Ctrl-Shift-a>', 'fake-key <Ctrl-a>', mode='insert')
bind('<Ctrl-k>', 'fake-key <Home><Shift-End><Delete>', mode='insert')

#######################
# Command Mode
#######################

# Exit command mode
bind('<Ctrl-c>', 'mode-enter normal', mode='command')
bind('<Ctrl-t>', 'fake-key -g <Enter>', mode='command')

#######################
# Theme
#######################
c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.policy.images = 'never'
config.source('themes/nord-qutebrowser.py')

# Force dark mode
bind('sd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/usercss/solarized/solarized-dark-all-sites.css ""')
