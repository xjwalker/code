class Multiset:
    multi_set = []
    repeated = set()

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        value_in_multiset = False
        if val in self.repeated:
            pass
        else:
            repeated_value = False

        for i in range(len(self.multi_set)):
            if val == self.multi_set[i]:
                value_in_multiset = True
                break
        if value_in_multiset and not repeated_value:
            self.multi_set.append(val)
            self.repeated.add(val)
        if not value_in_multiset:
            self.multi_set.append(val)
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        updated = False
        for i in range(len(self.multi_set) - 1, 0, -1):
            if val == self.multi_set[i]:
                updated = True
                if len(self.multi_set) > 2:
                    new_multiset = []
                else:
                    new_multiset = self.multi_set[:i] + self.multi_set[i + 1:]

        if updated:
            self.multi_set = new_multiset
            if val in self.repeated:
                self.repeated.remove(val)

        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        for i in range(len(self.multi_set)):
            if val == self.multi_set[i]:
                return True
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.multi_set)