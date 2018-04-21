set encoding=utf-8 fileencodings=ucs-bom,utf-8,cp936

set termguicolors

set nocompatible " be iMproved, required
filetype off " required
set nowrapscan

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
""""""""""""""""""""""""""""""
"welcome page
"Plugin 'mhinz/vim-startify'

"syntax highlight
Plugin 'kien/rainbow_parentheses.vim'
Plugin 'suan/vim-instant-markdown'
Plugin 'posva/vim-vue'

"auto complete
Plugin 'mattn/emmet-vim'
Plugin 'tpope/vim-surround'
if has('python3')
Plugin 'davidhalter/jedi-vim'
Plugin 'SirVer/ultisnips'
endif

"gramma
Plugin 'w0rp/ale'
"Plugin 'walm/jshint.vim'
"Plugin 'nvie/vim-flake8'

"css/less/sass/html color preview
Plugin 'gorodinskiy/vim-coloresque'

"color/theme
" Plugin 'flazz/vim-colorschemes'
Plugin 'chriskempson/base16-vim'
Plugin 'bling/vim-airline'
Plugin 'kabbamine/vcoolor.vim'

"unsorted
Plugin 'tpope/vim-unimpaired'
Plugin 'guns/vim-sexp'
Plugin 'dhruvasagar/vim-table-mode'
"Plugin 'jelera/vim-javascript-syntax'
Plugin 'Yggdroot/indentLine'
Plugin 'terryma/vim-multiple-cursors'
Plugin 'honza/vim-snippets'
Plugin 'kien/ctrlp.vim'
Plugin 'majutsushi/tagbar'
""""""""""""""""""""""""""""""
call vundle#end()

filetype plugin indent on " required

" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
" :PluginUpdate     - Update all configured bundles; press 'u' after complete to see changelog, 'l' to see error list
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

""""""""""""""""""""""BASE CONFIG"""""""""""""""""""""""

set nobackup
set noswapfile
set noundofile

set laststatus=2

syntax enable
syntax on

" vimrc文件修改之后自动加载
autocmd! bufwritepost .vimrc source %

" 文件修改之后自动载入
set autoread

" 高亮搜索命中的文本
set hlsearch

" 随着键入即时搜索
set incsearch

" 搜索时忽略大小写
set ignorecase

" 有一个或以上大写字母时仍大小写敏感
set smartcase

set guifont=Menlo:h14

colorscheme base16-irblack

" 在状态栏显示正在输入的命令
set showcmd

" 显示括号配对情况
set showmatch

" :next, :make 命令之前自动保存
set autowrite

" 允许使用鼠标
set mouse=a

" 设置行号
set nu

" 退格键可用
set backspace=2

" 退格键一次删掉4个空格
set smarttab

" 缩进
set autoindent
set smartindent

" 保存文件时自动删除行尾空格或Tab
autocmd BufWritePre * :%s/\s\+$//e

" 保存文件时自动删除末尾空行
autocmd BufWritePre * :%s/^$\n\+\%$//ge

" 填充Tab
set expandtab
set tabstop=4
set shiftwidth=4
set shiftround

" 代码折叠 光标在缩进下方时用za命令折叠或展开
set fdm=indent
" 默认展开
set foldlevel=99

"""""""""""""""""""""""""KEY MAPPING""""""""""""""""""""
" F2切换行号显示
nnoremap <F2> :set nonu!<CR>:set foldcolumn=0<CR>

" F3打开目录树
"nmap <silent> <F3> :NERDTreeToggle<CR>

" F4显示TagList
nmap <silent> <F4> :TagbarToggle<CR>

" <F6> 新建标签页
"map <F6> <Esc>:tabnew<CR>

" <F7> 拷贝粘贴代码不破坏缩进
set pastetoggle=<F7>

"disable arrow keys
noremap <Up> <Nop>
noremap <Down> <Nop>
noremap <Left> <Nop>
noremap <Right> <Nop>

" 在Normal Mode和Visual/Select Mode下，利用Tab键和Shift-Tab键来缩进文本
nnoremap > >>
nnoremap < <<
vnoremap > >gv
vnoremap < <gv

" 左右分割窗口Ctrl+w +v
" 上下分割窗口Ctrl+w +s
" 关闭窗口Ctrl+w  +q

" quicker window switching
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" quicker window resize
nnoremap <C-Enter> <C-w>=
nnoremap <C-Left> <C-w><
nnoremap <C-Right> <C-w>>
nnoremap <C-Up> <C-w>+
nnoremap <C-Down> <C-w>-

""""""""""""""""""""""""""""""PLUGIN CONFIG""""""""""""""""""""""""""

"netrw
let g:netrw_banner = 0 "no banner
let g:netrw_browse_split = 3 "in new tab
let g:netrw_winsize = 25 "25% of the page
let g:netrw_liststyle = 3 "what's this
let g:netrw_altv = 1 "what's this

"let g:UltiSnipsSnippetDirectories=["UltiSnips"]

" CtrlP
let g:ctrlp_show_hidden = 1
let g:ctrlp_cmd = 'CtrlPMixed'

" instant-markdown
let g:instant_markdown_slow = 1

" manual load :InstantMarkdownPreview
let g:instant_markdown_autostart = 0

" airline
let g:airline_section_y = '%{strftime("%H:%M")}'
" 开启tabline
let g:airline#extensions#tabline#enabled = 1
" tabline中当前buffer两端的分隔字符
let g:airline#extensions#tabline#left_sep = ' '
" tabline中未激活buffer两端的分隔字符
let g:airline#extensions#tabline#left_alt_sep = '|'
" tabline中buffer显示编号
let g:airline#extensions#tabline#buffer_nr_show = 1

" jedi
autocmd FileType python3 setlocal completeopt-=preview
let g:jedi#completions_command = "<C-n>"

" flake8
" let g:flake8_show_in_file = 1
" let g:flake8_show_in_gutter = 1
" autocmd! BufRead,BufWritePost *.py call Flake8()
" let g:syntastic_python_checkers=['flake8']
" let g:syntastic_python_flake8_args='--ignore=E501'

" ultisnips
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"

" jshint
"autocmd! BufRead,BufWritePost *.js :JSHint

" vim-table-mode: markdown
let g:table_mode_corner="|"

" rainbow_parentheses
let g:rbpt_colorpairs = [
    \ ['brown',       'RoyalBlue3'],
    \ ['Darkblue',    'SeaGreen3'],
    \ ['darkgray',    'DarkOrchid3'],
    \ ['darkgreen',   'firebrick3'],
    \ ['darkcyan',    'RoyalBlue3'],
    \ ['darkred',     'SeaGreen3'],
    \ ['darkmagenta', 'DarkOrchid3'],
    \ ['brown',       'firebrick3'],
    \ ['gray',        'RoyalBlue3'],
    \ ['darkmagenta', 'DarkOrchid3'],
    \ ['Darkblue',    'firebrick3'],
    \ ['darkgreen',   'RoyalBlue3'],
    \ ['darkcyan',    'SeaGreen3'],
    \ ['darkred',     'DarkOrchid3'],
    \ ['red',         'firebrick3'],
    \ ]

let g:rbpt_max = 16
let g:rbpt_loadcmd_toggle = 0
au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces

" vCoolor.vim
let g:vcoolor_map = '<leader>cp'
let g:vcool_ins_rgb_map = '<leader>cpr'       " Insert rgb color.
let g:vcool_ins_hsl_map = '<leader>cph'       " Insert hsl color.
let g:vcool_ins_rgba_map = '<leader>cpra'      " Insert rgba color.

" emmit prefix
let g:user_emmet_leader_key = '<C-y>'
let g:user_emmet_install_global = 0
autocmd FileType html,css EmmetInstall

function! s:base16_customize() abort
  call Base16hi("MatchParen", g:base16_gui05, g:base16_gui03, g:base16_cterm05, g:base16_cterm03, "bold,italic", "")
endfunction

augroup on_change_colorschema
  autocmd!
  autocmd ColorScheme * call s:base16_customize()
augroup END

" ale and langs
" https://github.com/w0rp/ale
" https://prettier.io/docs/en/vim.html
"""""""""""""""""""""""""""""""""""""""
" manual
" :ALELint
" :ALEFix

" bed into Airline
let g:airline#extensions#ale#enabled = 1
let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'

" customized statusline
" :help ale#statusline#Count()

" :help ale-navigation-commands
nmap <silent> <C-k> <Plug>(ale_previous_wrap)
nmap <silent> <C-j> <Plug>(ale_next_wrap)

" don't lint on 'open' or 'edit', but on 'save'
let g:ale_lint_on_enter = 0
let g:ale_lint_on_text_changed = 'never' " ['never' | 'normal']
let g:ale_fix_on_save = 1

" route to npm ['eslint' | 'prettier' | 'standard']
let g:ale_fixers = {}
let g:ale_fixers['javascript'] = ['prettier']

" pass arg-string to cli
"let g:ale_javascript_prettier_options = '--single-quote --trailing-comma es5'

" use local config
"let g:ale_javascript_prettier_use_local_config = 1

" add a key map to 'gp'
"nnoremap gp :silent %!prettier --stdin --trailing-comma all --single-quote

" use quickfix instead of loclist
"let g:ale_set_loclist = 0
"let g:ale_set_quickfix = 1

" show warn and err in a window, and keep it open
"let g:ale_open_list = 1
"let g:ale_keep_list_window_open = 1

" default layout: horizontal
"let g:ale_list_vertical = 1

" Show 5 lines of errors (default: 10)
" let g:ale_list_window_size = 5
"""""""""""""""""""""""""""""""""""""""
