# Matugen generated colors for qutebrowser

# Webpage background (Dark mode support)
c.colors.webpage.bg = "{{ colors.background.default.hex }}"
c.colors.webpage.preferred_color_scheme = "dark"
c.colors.webpage.darkmode.enabled = (
    True  # Optional, falls du echtes Dark-Theming willst
)

# Completion (Vorschläge in der Befehlszeile)
c.colors.completion.category.bg = "{{ colors.surface_container_highest.default.hex }}"
c.colors.completion.category.fg = "{{ colors.primary.default.hex }}"
c.colors.completion.category.border.top = (
    "{{ colors.surface_container_highest.default.hex }}"
)
c.colors.completion.category.border.bottom = (
    "{{ colors.surface_container_highest.default.hex }}"
)
c.colors.completion.even.bg = "{{ colors.surface.default.hex }}"
c.colors.completion.odd.bg = "{{ colors.surface_container_low.default.hex }}"
c.colors.completion.fg = "{{ colors.on_surface.default.hex }}"
c.colors.completion.item.selected.bg = "{{ colors.primary.default.hex }}"
c.colors.completion.item.selected.fg = "{{ colors.on_primary.default.hex }}"
c.colors.completion.match.fg = "{{ colors.tertiary.default.hex }}"
c.colors.completion.scrollbar.bg = "{{ colors.surface.default.hex }}"
c.colors.completion.scrollbar.fg = "{{ colors.primary.default.hex }}"

# Context menu
c.colors.contextmenu.menu.bg = "{{ colors.surface.default.hex }}"
c.colors.contextmenu.menu.fg = "{{ colors.on_surface.default.hex }}"
c.colors.contextmenu.selected.bg = "{{ colors.primary.default.hex }}"
c.colors.contextmenu.selected.fg = "{{ colors.on_primary.default.hex }}"

# Downloads
c.colors.downloads.bar.bg = "{{ colors.surface.default.hex }}"
c.colors.downloads.start.bg = "{{ colors.primary.default.hex }}"
c.colors.downloads.start.fg = "{{ colors.on_primary.default.hex }}"
c.colors.downloads.stop.bg = "{{ colors.tertiary_container.default.hex }}"
c.colors.downloads.error.bg = "{{ colors.error.default.hex }}"
c.colors.downloads.error.fg = "{{ colors.on_error.default.hex }}"

# Hints (Die Buchstaben zum Springen)
c.colors.hints.bg = "{{ colors.primary.default.hex }}"
c.colors.hints.fg = "{{ colors.on_primary.default.hex }}"
c.colors.hints.match.fg = "{{ colors.secondary_fixed_dim.default.hex }}"

# Statusbar
c.colors.statusbar.normal.bg = "{{ colors.surface.default.hex }}"
c.colors.statusbar.normal.fg = "{{ colors.on_surface.default.hex }}"
c.colors.statusbar.insert.bg = "{{ colors.tertiary.default.hex }}"
c.colors.statusbar.insert.fg = "{{ colors.on_tertiary.default.hex }}"
c.colors.statusbar.command.bg = "{{ colors.surface.default.hex }}"
c.colors.statusbar.command.fg = "{{ colors.on_surface.default.hex }}"
c.colors.statusbar.url.success.https.fg = "{{ colors.primary.default.hex }}"
c.colors.statusbar.url.hover.fg = "{{ colors.secondary.default.hex }}"

# Tabs (Hier habe ich den "Waybar-Look" eingebaut)
c.colors.tabs.bar.bg = "{{ colors.surface.default.hex }}"
c.colors.tabs.even.bg = "{{ colors.surface_container_low.default.hex }}"
c.colors.tabs.even.fg = "{{ colors.on_surface_variant.default.hex }}"
c.colors.tabs.odd.bg = "{{ colors.surface_container_low.default.hex }}"
c.colors.tabs.odd.fg = "{{ colors.on_surface_variant.default.hex }}"
c.colors.tabs.selected.even.bg = "{{ colors.primary.default.hex }}"
c.colors.tabs.selected.even.fg = "{{ colors.on_primary.default.hex }}"
c.colors.tabs.selected.odd.bg = "{{ colors.primary.default.hex }}"
c.colors.tabs.selected.odd.fg = "{{ colors.on_primary.default.hex }}"
c.colors.tabs.indicator.start = "{{ colors.primary.default.hex }}"
c.colors.tabs.indicator
