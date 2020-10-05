"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

class QueueClass:
    def __init__(self):
        self.elems1 = []
        self.elems2 = []
        self.elems3 = []

    def is_empty(self):
        return self.elems1 == []

    def to_queue(self, item):
        self.elems1.insert(0, item)

    def from_queue(self):
        return self.elems1.pop()

    def size(self):
        return len(self.elems1)

    def done(self):
        x = self.elems1.pop()
        self.elems2.insert(0, x)

    def not_done(self):
        x = self.elems1.pop()
        self.elems3.insert(0, x)

    def revision(self):
        x = self.elems3.pop()
        self.elems2.insert(0,x)

qc_obj = QueueClass()
qc_obj.to_queue(2)
qc_obj.to_queue(14)
qc_obj.to_queue(123)
qc_obj.to_queue(222)
qc_obj.done()
print(qc_obj.elems1)
print(qc_obj.elems2)
qc_obj.not_done()
qc_obj.not_done()
qc_obj.revision()
print(qc_obj.elems1)
print(qc_obj.elems2)
print(qc_obj.elems3)