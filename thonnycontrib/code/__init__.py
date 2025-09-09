from thonny import get_workbench,Workbench
from thonny.workbench import SyntaxThemeSettings


def vs_code_theme() -> SyntaxThemeSettings:
    default_fg = "#cccccc"
    default_bg = "#1F1F1F"
    string_fg = "#ce9178"
    open_string_bg = "#342424"
    gutter_foreground = "#6e7681"
    gutter_background = "#1F1F1F"
    blue_like_fg = "#569cd6"
    
    # s.configure("Local.Code", foreground="#BCCAE8")
    # s.configure("MatchedName.Code", background="#193022")

    return {
    "TEXT": {
        "foreground": default_fg,
        "insertbackground": default_fg,
        "background": default_bg,
    },
    "GUTTER": {"foreground": gutter_foreground, "background": gutter_background},
    "breakpoint": {"foreground": "#e51400"},
    "current_line": {"background": "#363636"},
    "sel": {"foreground":"#FFFF","background": "#264f78"},
    "definition": {"foreground": "#9cdcfe"},
    "class_definition": {"foreground":"#4ec9b0","background":None},
    "function_definition": {"foreground":"#dcdcaa","background":None},
    "string": {"foreground": string_fg},
    "string3": {"foreground": string_fg, "background": None},
    "open_string": {"foreground": string_fg, "background": open_string_bg},
    "open_string3": {
      "foreground": string_fg,
      "background": open_string_bg,
    },
    "builtin": {"foreground": "#dcdcaa"},
    "keyword": {"foreground": blue_like_fg},
    "number": {"foreground": "#b5cea8"},
    "comment": {"foreground": "#6a9955"},
    "welcome": {"foreground": "#3b8eea"},
    "magic": {"foreground": "#3b8eea"},
  }

def vs_tags_colors():
  ...
def main(wb:Workbench):
  wb.add_syntax_theme("Vscode","Default Dark",vs_code_theme)
  wb.bind("EditorContentChanged", vs_tags_colors)

def load_plugin():
  main(get_workbench())