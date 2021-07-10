from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console: Console = Console()


def make_style_prompt(choices: list, default: str = None, main_style: str = "none", frame_style: str = "none",
                      frame_border_style: str = "none") -> str:
    """
    Prompts user in a cool way and retrieves what the user picked.

    :param choices: A list of choices.
    :param default: The value that gets returned if user doesn't type anything in.
    :param main_style: The main theme/color of the prompt.
    :param frame_style: The theme/color for the text in the panels.
    :param frame_border_style: The theme/color for the frame in the panels.
    :return: str value of final style choice the user selected.
    """
    choices = [str(i) for i in choices]
    if default is not None:
        # Get index of default so it can be set to the default choice.
        default_index = str(choices.index(default) + 1)
    else:
        default_index = None

    choices_styled = []
    c = 0
    for i in choices:
        c += 1
        # choices_styled.append(Panel(str(c) + ". " + i, style=frame_style, border_style=frame_border_style))
        choices_styled.append(Panel(f"{c}. {i}", style=frame_style, border_style=frame_border_style))

    console.print(Panel(Markdown("**Would you like to:**"), style=main_style, border_style=main_style))
    for i in choices_styled:
        console.print(i)

    choice_index = Prompt.ask(Text.assemble(("╰>", main_style)), choices=[str(x) for x in range(1, c + 1)],
                              default=default_index)
    choice_index = int(choice_index)
    return choices[choice_index - 1]
