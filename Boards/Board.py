import BoardDB


class QuestBoard:

    def __init__(self, author, title, content):
        self._QuestAuthor = author
        self._QuestTitle = title
        self._QuestContent = content
        self._QuestID = 0

    def make_quest(self):
        B_DB = BoardDB()
        self._QuestID = B_DB.new_question((self._QuestAuthor, self._QuestTitle, self._QuestContent))

    def edit_quest(self, newTitle, newContent):
        B_DB = BoardDB()
        B_DB.edit_question(self._QuestID, newTitle, newContent)

    def delete_quest(self):
        B_DB = BoardDB()
        B_DB.delete_question(self._QuestID)

    def list_quest(self, author):
        B_DB = BoardDB
        DATA = B_DB.question_list(author)



class AnwBoard:
    def __init__(self, quest_id, author, Answer):
        self._quest_ID = quest_id
        self._AnswerAuthor = author
        self._AnswerContent = Answer

    def make_anw(self):
        B_DB = BoardDB()
        B_DB.new_answer(self._quest_ID, self._AnswerAuthor, self._AnswerContent)

    def edit_quest(self, newContent):
        B_DB = BoardDB()
        B_DB.edit_question(self._QuestID, newContent)

    def delete_quest(self):
        B_DB = BoardDB()
        B_DB.delete_question(self._QuestID)

    def list_anw(self, author):
        B_DB = BoardDB()
        DATA = B_DB.anwser_list(author)

    def list_anw_quest(self, ID):
        B_DB = BoardDB()
        DATA = B_DB.answer_list_by_question(ID)