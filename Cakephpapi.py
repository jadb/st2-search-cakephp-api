# Written by Jad Bitar (@jadb / www.jadbitar.com)

# available commands
#   cakephpapi_search_selection
#   cakephpapi_search_from_input

# changelog
# Jad Bitar - first implementation of search selection and search from input

import sublime
import sublime_plugin

import subprocess
import webbrowser

def SearchFor(text):
    url = 'http://api20.cakephp.org/search/' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class CakephpapiSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)

            SearchFor(text)

class CakephpapiSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search CakePHP API for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
