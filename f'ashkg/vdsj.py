class Marks:

  def srckpi(self):
    return (sum([i for i in self.kpi.values()]))/len(self.kpi)


class Student(Marks):

  def init(self, name, lastname, group, kpi):
    self.name = name
    self.lastname = lastname
    self.group = group
    self.kpi = kpi

  def eq(self, other):
    return self.srckpi() == other.srckpi()

  def lt(self, other):
    return self.srckpi() < other.srckpi() 

  def gt(self, other):
    return self.srckpi() > other.srckpi()

  def le(self, other):
    return self.srckpi() <= other.srckpi() 

  def ge(self, other):
    return self.srckpi() >= other.srckpi()

s1 = Student('Neu', 'Polo', 'Prima', {'math': 100, 'history': 89, 'literature': 88})

s2 = Student('Neu1', 'Polo1', 'Prima1', {'math': 98, 'history': 86, 'literature': 94})
print(s2==s1)
print(s2>s1)
print(s2<s1)
print(s2<=s1)
print(s2>=s1)
