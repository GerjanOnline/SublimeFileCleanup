import sublime
import sublime_plugin


class FileCleanupCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.run_command("unexpand_tabs")

        self.view.run_command("delete_trailing_spaces")

        sublime.status_message("File cleaned up!")
