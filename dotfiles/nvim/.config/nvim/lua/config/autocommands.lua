vim.api.nvim_create_autocmd('TextYankPost', {
    desc = 'Highlight when yanking (copying) text',
    group = vim.api.nvim_create_augroup('kickstart-highlight-yank', { clear = true }),
    callback = function()
        vim.highlight.on_yank()
    end,
})

vim.api.nvim_create_autocmd("BufWritePre", {
    pattern = "*",
    callback = function(args)
        require("conform").format({ bufnr = args.buf })
    end,
})


-- Automatically set cwd to the project root (nearest CMakeLists.txt or .git)
vim.api.nvim_create_autocmd("BufEnter", {
    pattern = "*",
    callback = function()
        local root = vim.fs.find({ "CMakeLists.txt", ".git" }, { upward = true })[1]
        print(root)
        if root then
            vim.cmd("cd " .. vim.fs.dirname(root))
        end
    end,
})
