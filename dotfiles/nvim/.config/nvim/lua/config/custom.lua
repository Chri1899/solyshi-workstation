-- Funktion zum Entfernen der Hintergründe
local function fix_transparency()
    local groups = {
        "Normal", "NormalNC", "Comment", "Constant", "Special", "Identifier",
        "Statement", "PreProc", "Type", "Underlined", "Todo", "String",
        "Function", "Conditional", "Repeat", "Operator", "Structure",
        "LineNr", "NonText", "SignColumn", "CursorLine", "CursorLineNr",
        "StatusLine", "StatusLineNC", "WinBar", "WinBarNC", "EndOfBuffer",
        "TreesitterContext", "NormalFloat", "FloatBorder"
    }
    for _, group in ipairs(groups) do
        vim.api.nvim_set_hl(0, group, { bg = "none", ctermbg = "none" })
    end
end

-- Führe es jetzt aus UND jedes Mal, wenn das Colorscheme wechselt
fix_transparency()
vim.api.nvim_create_autocmd("ColorScheme", {
    callback = fix_transparency,
})
