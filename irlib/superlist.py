''' 
Informations Retrieval Library
==============================
SuperList is an alternatice to Python's default lists (arrays) 
'''

# Author: Tarek Amr <@gr33ndata> 

class SuperList(list):
    ''' SuperList: An alternatice to Python's default lists (arrays)
        So that we can add some helper methods and functionalities.
    '''

    def unique_append(self, item):
        ''' Only append item to list if not already there, 
            In case we want our list to act like a set.
            Returns the index of the the added item'''
        if self.__contains__(item):
            return self.index(item)
        else:
            self.append(item)
            return len(self) - 1

    def expand(self, new_len=0, padding_data=float(0)):
		''' Expand a list size to new_len, 
            then fill new cells with padding_data. 
            The defaul padding_data is float(0).'''
		for i in range(len(self),new_len):
			self.append(padding_data)

    def insert_after_padding(self, index, item, padding_data=float(0)):
		''' Add item in specific index location, and expand if needed. 
            Notice that the original insert method for lists, 
            just adds items to end of list if index is bigger than length.
            Also, unlike the original list insert method,
            if there is existing item at index, it is overwritten.  
		'''
		self.expand(new_len=index+1, padding_data=padding_data)
		self[index] = item

    def increment_after_padding(self, index, item, padding_data=float(0)):
		''' Just like insert_after_padding().  
            However, existing items at index are incremented.  
		'''
		self.expand(new_len=index+1, padding_data=padding_data)
		self[index] = self[index] + item

    # We need to implement this
    # def populate_in_order(self, item, less_than):
    
    def populate_in_reverse_order(self, item, greater_than):
        ''' Add items to list, but in order
            Here we make sure bigger items are put at the beginning of list,
            greater_than is the function used to compare items
        '''
        if self == []:
            self.append(item)
        elif greater_than(item,self[0]):
            self.insert(0,item)
        else:
            for j in range(0,len(self)):
                if greater_than(item,self[j]):
                    self.insert(j,item)
                    break
            else:
                self.append(item)


if __name__ == '__main__':
    
    pass