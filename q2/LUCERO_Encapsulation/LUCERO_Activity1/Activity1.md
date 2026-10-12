1. A GameCharacter class has a username that can be displayed and accessed by anyone.

    -- Access Level: Public (+)

       Python Statement: self.username = username


2. A BankAccount class has a balance that should NOT be accessed directly outside the class.

    -- Access Level: Private (-)

       Python Statement: self.__balance = balance


3. A Vehicle class has an engineCode that should only be accessed within the class and its subclasses.

    -- Access Level: Protected (#)

       Python Statement: self._engineCode = engineCode


4. A Student class has a schoolName that is safe for everyone to view and modify.

    -- Access Level: Public (+)

       Python Statement: self.schoolName = schoolName


5. A VotingSystem class has a voterID that must be hidden for security reasons.

    -- Access Level: Private (-)

       Python Statement: self.__voterID = voterID