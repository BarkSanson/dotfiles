local mapper = {}

function mapper.noremap(mode, shortcut, command)
    vim.api.nvim_set_keymap(mode, shortcut, command , 
        {noremap = true, silent = true})
end

function mapper.map(mode, shortcut, command)
    vim.api.nvim_set_keymap(mode, shortcut, command, 
        {noremap = false})
end

function mapper.nnoremap(shortcut, command)
    mapper.noremap('n', shortcut, command)
end

function mapper.inoremap(shortcut, command)
    mapper.noremap('i', shortcut, command)
end

function mapper.nmap(shortcut, command)
    mapper.map('n', shortcut, command)
end

function mapper.xmap(shortcut, command)
    mapper.map('x', shortcut, command)
end

function mapper.omap(shortcut, command)
    mapper.map('o', shortcut, command)
end

return mapper
