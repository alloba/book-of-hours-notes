import yaml
import pathlib

from typing import List


def load_yaml(filepath: str):
    try:
        with open(filepath, 'w') as file_raw:
            return yaml.safe_load(file_raw)
    except Exception as e:
        raise e


def filter_ignored_dirs(files_list: List[pathlib.Path], ignored_dirs_list: List[pathlib.Path]):
    filter_files = []
    ignored_files = []
    for file in files_list:
        if not file.is_file():
            ignored_files.append(file)
            continue
        match = False
        for c in ignored_dirs_list:
            if c in file.parents:
                match = True
                break
        if not match:
            filter_files.append(file)
        else:
            ignored_files.append(file)
    return filter_files, ignored_files


def does_file_have_frontmatter(file_object):
    with open(file_object, 'r') as f:
        text = f.read()
        first_occur = text.find("---")
        second_occur = text.find("---", first_occur+1)

        if first_occur != 0 and second_occur != -1:
            print('WARN - frontmatter symbols may have been found, but they are not at the top: ' + str(file_object))
            return False
        if first_occur == -1 or second_occur == -1:
            return False
        else:
            return True


def fetch_frontmatter(file_object):
    with open(file_object, 'r') as f:
        text = f.read()
        first_occur = text.find("---")
        second_occur = text.find("---", first_occur+1)
        if first_occur != 0:
            raise Exception('Front matter symbols may have been found, but not in the correct location: ' + file_object)
        if first_occur == -1 or second_occur == -1:
            raise Exception('Frontmatter was not found (no paired --- symbols in file)')
        return str(text[first_occur+3: second_occur].strip())


def squishify_frontmatter(yaml_string: str):
    yaml_dict = yaml.safe_load(yaml_string)
    squished_yaml = {'tags': []}
    if yaml_dict is None:
        return ''

    try:
        for x in yaml_dict:
            if x == 'tags':
                squished_yaml['tags'].extend(yaml_dict['tags'])
            if x == 'aspects':
                if yaml_dict[x] is None:
                    continue
                for z in yaml_dict['aspects']:
                    clean_name = z['name']
                    clean_name = clean_name.replace(':', '/').replace(' ', '_')  # tags cant have spaces ;(

                    squished_yaml['tags'].append(""+clean_name+""+'/'+str(z['amount']))
    except Exception as e:
        print("failed to operate on: " + str(yaml_dict))
        raise e
    return yaml.dump(squished_yaml)


def strip_frontmatter(text: str):
    first_occur = text.find("---")
    second_occur = text.find("---", first_occur+1)
    if first_occur != 0:
        raise Exception('Front matter symbols may have been found, but not in the correct location')
    if first_occur == -1 or second_occur == -1:
        raise Exception('Frontmatter was not found (no paired --- symbols in file)')

    return text[second_occur+3:]


def replace_frontmatter(file_object):
    if not does_file_have_frontmatter(file_object):
        raise Exception('cannot replace frontmatter when none is detected: ' + file_object)
    old_front = fetch_frontmatter(file_object)
    new_front = squishify_frontmatter(old_front)
    new_dump = yaml.dump(new_front)

    complete_text = ''
    with open(file_object, 'r') as f:
        complete_text = f.read()
    if complete_text == '':
        raise Exception('Got a blank string when loading file: ' + file_object)
    new_total = strip_frontmatter(complete_text) #complete_text.replace(old_front, new_dump)
    new_total = '---\n' + new_front + '---\n' + new_total
    # return new_total

    with open(file_object, 'w') as f:
        f.write(new_total)

def get_target_files():
    base_vault_path = '../'
    ignored_subdirectories_paths = [
        '.obsidian',
        '.gitignore',
        '_dataview_reference',
        '_queries',
        '_scripts',
        '_templates',
        'venv',
        '.idea',
        '.git'
    ]

    source_dir = pathlib.Path(base_vault_path)
    ignored_dirs = [source_dir.joinpath(x) for x in ignored_subdirectories_paths]

    files_generator = source_dir.rglob("*")

    all_files = list(files_generator)
    filtered_files = filter_ignored_dirs(all_files, ignored_dirs)[0]
    return filtered_files

def convert_all_aspects_everywhere_to_tags():
    for f in get_target_files():
        if does_file_have_frontmatter(str(f.resolve())):
            print(str(f.resolve()))
            replace_frontmatter(str(f.resolve()))

def validate_aspects():
    def validation_copy(file_object):
        # This is just a subset of the rewrite function with some tweaks.
        try:
            if not does_file_have_frontmatter(file_object):
                raise Exception('cannot replace frontmatter when none is detected: ' + file_object)
            old_front = fetch_frontmatter(file_object)
            new_front = squishify_frontmatter(old_front)
            new_dump = yaml.dump(new_front)

            complete_text = ''
            with open(file_object, 'r') as f:
                complete_text = f.read()
            if complete_text == '':
                raise Exception('Got a blank string when loading file: ' + file_object)
            new_total = strip_frontmatter(complete_text) #complete_text.replace(old_front, new_dump)
        except Exception as e:
            return {'state':'failed', 'file': str(file_object.resolve()), 'message': str(e)}
        return {'state':'passed', 'file': str(file_object.resolve()), 'message': ''}

    files = get_target_files()
    results = []
    for f in files:
        results.append(validation_copy(f))

    failed = [x for x in results if x['state'] == 'failed']
    print('\n\n')
    for e in failed:
        print(str(e))

if __name__ == '__main__':
    validate_aspects()
#    convert_all_aspects_everywhere_to_tags()
