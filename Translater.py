import os
import yaml


class Translater:
    """translated class"""

    def __init__(self):
        self.origin_path = 'data/origin/'
        self.translated_path = 'data/translated/'

    def run(self):
        print("Started")
        for root, dirs, files in os.walk(self.origin_path, topdown=False):
            for name in files:

                f = open(os.path.join(root, name), 'r', encoding='utf-8-sig')

                translated_text = self.translate(f.read())

                new_dir = os.path.join(self.translated_path, os.path.dirname(f.name.replace(self.origin_path, '')))

                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)

                new_file = os.path.join(new_dir, os.path.basename(name))

                f = open(new_file, 'w', encoding='utf-8-sig')

                f.write(translated_text)
                f.close()

    def translate(self, text):
        return self.translated_path
