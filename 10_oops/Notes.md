CLASS
├── Constructor (**init**)
│ ├── Runs automatically when object created
│ ├── Sets up initial attributes
│ └── def **init**(self, params):
│
├── Attributes (self.x)
│ ├── Data stored on the object
│ └── Each object has its OWN copy
│
└── Methods (def name(self):)
├── Actions the object can perform
└── Always have self as first parameter

🎓 THE GOLDEN RULES
RULE 1: Every method ALWAYS has self as first parameter
def any_method(self, ...):

RULE 2: Attributes go in **init**
self.name = name (DATA)

RULE 3: Methods are ACTIONS that take parameters
def deposit(self, amount): (ACTION + DATA needed)

RULE 4: To actually change data, use self.x = new_value
self.age += 1 (not just print age + 1)

RULE 5: Condition for insufficient funds:
if amount > self.balance: (trying to take MORE than available)

You DEFINE methods with self
You CALL methods without self
