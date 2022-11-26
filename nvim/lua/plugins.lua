local Plug = vim.fn['plug#']

vim.call('plug#begin', '~/.config/nvim/plugged')

Plug 'neovim/nvim-lspconfig'
Plug 'ms-jpq/coq_nvim'
Plug 'ms-jpq/coq.artifacts'
Plug 'windwp/nvim-autopairs'
Plug 'folke/tokyonight.nvim'
Plug 'williamboman/mason.nvim'
Plug 'EdenEast/nightfox.nvim'

vim.call('plug#end')

require("nvim-autopairs").setup {}
require("plugins/tokyonight-config")
require("mason").setup()
vim.g.coq_settings = { auto_start = 'shut-up'}
