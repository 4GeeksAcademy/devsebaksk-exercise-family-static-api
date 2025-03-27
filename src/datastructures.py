
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member(ok): Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member(ok): Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
            "first_name":"John",
            "id":1,
            "age":33,
            "lucky_numbers":[7,13,22]
            },
            {
            "first_name":"Jane",
            "id":2,
            "age":35,
            "lucky_numbers":[10,14,3]
            },
            {
            "first_name":"Jimmy",
            "id":3,
            "age":5,
            "lucky_numbers":[1]
            }
            ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        miembro = list(filter(lambda x: x['id'] == id, self._members))
        x = self._members.index(miembro[0])
        del self._members[x]
        return 'done'

    def get_member(self, id):
        # fill this method and update the return
        for x in self._members:
            if x["id"] == int(id):
                member = dict(x)
                return member
        #miembro = dict(filter(lambda x: x["id"] == id, self._members))
        return 'none'

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
