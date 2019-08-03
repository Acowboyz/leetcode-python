import requests
import os
import time


class Config(object):
    """
    some config setup, such as your github page
    １．  local path
    ２．　leetcode path at github
    """

    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    leetcode_algorithms_path = os.path.join(root_path, 'leetcode-algorithms')

    readme_path = os.path.join(root_path, 'README.md')

    github_leetcode_url = 'https://github.com/Acowboyz/leetcode-python/blob/master/leetcode-algorithms'

    leetcode_url = 'https://leetcode.com/problems/'

    leetcode_api_url = 'https://leetcode.com/api/problems/algorithms/'



class Question(object):
    """
    this class is used to store the information of each question
    """

    def __init__(self,
                 q_id,
                 q_name,
                 url,
                 q_lock,
                 q_difficulty):
        self.q_id = q_id
        self.title = q_name
        # the problem description url
        self.url = url
        # boolean，锁住了表示需要购买
        self.lock = q_lock
        self.difficulty = q_difficulty
        # the solution url
        self.sol_python = ''

    def __repr__(self):
        """
        :return:
        """
        return str(self.q_id) + ' ' + str(self.title) + ' ' + str(self.url)


class TableInform(object):
    def __init__(self):
        # raw questions information
        self.questions = []
        # this is table index
        self.table = []
        # this is the element of question
        self.table_item = {}
        self.locked = 0

    def _get_leetcode_problems(self):
        """
        used to get leetcode information
        :return:
        """
        # we should look the response data carefully to find law
        # return byte. content type is byte
        response = requests.get(Config.leetcode_api_url)
        # get all problems
        self.questions = response.json().get('stat_status_pairs')
        # print(self.questions)
        difficulty_list = ['Easy', 'Medium', 'Hard']
        for i in range(len(self.questions) - 1, -1, -1):
            question = self.questions[i]
            question_stat = question.get('stat')
            q_name = question_stat.get('question__title')
            q_url = question_stat.get('question__title_slug')
            q_id = str(question_stat.get('frontend_question_id')).zfill(4)

            q_lock = question.get('paid_only')
            if q_lock:
                self.locked += 1

            difficulty = difficulty_list[question['difficulty']['level'] - 1]
            url = f'{Config.leetcode_url}{q_url}/description/'
            q = Question(q_id, q_name, url, q_lock, difficulty)
            self.table.append(q.q_id)
            self.table_item[q.q_id] = q

    # create problems folders
    def _create_folder(self):
        algo_path = Config.leetcode_algorithms_path
        if os.path.exists(algo_path):
            print(algo_path, ' algorithms is already exits')
        else:
            print('creating {} folder....'.format(algo_path))
            os.mkdir(algo_path)

        for item in self.table_item.values():
            question_folder = os.path.join(algo_path, f'{item.q_id}. {item.title}')
            if os.name != 'posix':
                # 如果不是linux，那么就要吧后面的问号去掉
                question_folder = question_folder[:-1]
            if not os.path.exists(question_folder):
                print(question_folder + 'is not exits, create it now....')
                os.mkdir(question_folder)

    def update_table(self):
        # the complete inform should be update
        complete_info = CompleteInform()
        self._get_leetcode_problems()
        # the total problem nums
        complete_info.total = len(self.table)
        complete_info.lock = self.locked
        self._create_folder()
        algo_path = Config.leetcode_algorithms_path

        # get the list of folders
        folders = os.listdir(algo_path)

        for folder in folders:
            files = os.listdir(os.path.join(algo_path, folder))

            if not files:
                continue

            complete_info.complete_num += 1

            for file in files:
                # python file
                if file.endswith('.py'):
                    complete_info.solved['python'] += 1
                    # update problem inform
                    folder_url = folder.replace(' ', "%20")
                    folder_url = os.path.join(folder_url, file)
                    folder_url = os.path.join(Config.github_leetcode_url,
                                              folder_url)

                    self.table_item[folder[:4]].sol_python = f'[Python]({folder_url})'

        readme = Readme(complete_info.total,
                        complete_info.complete_num,
                        complete_info.lock,
                        complete_info.solved)

        readme.create_leetcode_readme([self.table, self.table_item])
        print('-------the complete inform-------')
        print(complete_info.solved)
        print('the total complete num is: {}'.format(
            complete_info.complete_num))


class CompleteInform(object):
    """
    this is statistic inform
    """

    def __init__(self):
        self.solved = {
            'python': 0,
        }
        self.complete_num = 0
        self.lock = 0
        self.total = 0

    def __repr__(self):
        return str(self.solved)


class Readme(object):
    """
    generate folder and markdown file
    update README.md when you finish one problem by some language
    """

    def __init__(self, total, solved, locked, others=None):
        """
        :param total: total problems nums
        :param solved: solved problem nums
        :param others:
        """
        self.total = total
        self.solved = solved
        self.others = others
        self.locked = locked
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.msg = '# Leetcode Python Challenge\n' \
                   'Until {}, I have solved **{}** / **{}** problems ' \
                   'while **{}** are still locked.' \
                   '\n\nCompletion statistic: ' \
                   '\n1. Python: {python}' \
                   '\n\nNote: :lock: means you need to buy a book from LeetCode\n'.format(
            self.time, self.solved, self.total, self.locked, **self.others)

    def create_leetcode_readme(self, table_instance):
        """
        create REAdME.md
        :return:
        """
        readme_path = Config.readme_path
        # write some basic information about leetcode
        with open(readme_path, 'w') as f:
            f.write(self.msg)
            f.write('\n----------------\n')

        with open(readme_path, 'a') as f:
            f.write('## LeetCode Solution Table\n')
            f.write('| ID | Title | Difficulty | Python |\n')
            f.write('|:---:' * 4 + '|\n')
            table, table_item = table_instance

            for index in table:
                item = table_item[index]
                if item.lock:
                    _lock = ':lock:'
                else:
                    _lock = ''
                data = {
                    'id': item.q_id,
                    'title': '[{}]({}) {}'.format(item.title, item.url, _lock),
                    'difficulty': item.difficulty,
                    'python': item.sol_python if item.sol_python else '---',
                }
                line = '|{id}|{title}|{difficulty}|{python}|\n'.format(**data)
                f.write(line)
            print('README.md was created.....')


def main():
    table = TableInform()
    table.update_table()


if __name__ == '__main__':
    main()
