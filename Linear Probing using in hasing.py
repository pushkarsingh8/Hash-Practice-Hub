#Basics Linear probing:-
class Dictionary:
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size # create a key section
        self.value = [None] * self.size #create a value section
    

    def put(self,key,value):
        hash_value = self.hash_funct(key)


        if self.slots[hash_value] == None: #location memory is Empty
            self.slots[hash_value] = key
            self.value[hash_value] = value


        else:
            if self.slots[hash_value] == key: #already key exist kardi hai with same key
                self.value[hash_value] = value

            else:

                new_hash_value = self.rehash(hash_value) #generate rehash value

            while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key: #if any thing found so it's break

                new_hash_value = self.rehash(new_hash_value) #counter 

                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.value[new_hash_value] = value

                else:
                    self.value[new_hash_value] = value
                    


    def __str__(self):
        
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(f"{self.slots[i]} : {self.value[i]}")

        return ""

    

    
    
    def hash_funct(self,key):
        return abs(hash(key)) % self.size #create a hash value for storing value 



    def rehash(self,old_hash_value):
        return  (old_hash_value + 1) % self.size #create a new Hash value +1 to update next number
    



    def __setitem__(self,key,value):
        return self.put(key,value)


d1 = Dictionary(4)

d1.put("key",0)
d1.put("harsh",25)
d1["Ram"] = 10
d1.put("krishna",63)

print(d1)



