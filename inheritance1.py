class university():
  universityName = "Punjabi University"
  def show_universityname(self):
    print(self.universityName)

  def __init__(self):
    print(self.universityName)

class engine(university):
  clgname = "EG1"
  def show_clg(self):
    print(self.clgname)

  def __init__(self):
      super().__init__()
      print(self.clgname)


class medical(university):
  clgname = "MD!"
  def show_clg(self):
    print(self.clgname)
  def __init__(self):
      super().__init__()
      print(self.clgname)


class dpone_engine(engine):
  dpname = "cse"
  def show_clg(self):
      print(self.dpname)
  def __init__(self):
      super().__init__()
      print(self.dpname)

class dptwo_engin(engine):
  dpname = "ME"
  def show_clg(self):
      print(self.dpname)

  def __init__(self):
      super().__init__()
      print(self.dpname)

class dpone_medical(medical):
  dpname = "Nursing"
  def show_clg(self):
      print(self.dpname)
  def __init__(self):
      super().__init__()
      print(self.dpname)

class dptwo_medical(medical):
  dpname = "LabTechnician"
  def show_clg(self):
      print(self.dpname)

  def __init__(self):
      super().__init__()
      print(self.dpname)


ram =dpone_engine()

# print(ram.universityName)
# print(ram.dpname)
# print(ram.clgname)

# sita= dptwo_medical()
# print(sita.clgname)
# print(sita.dpname)
# print(sita.universityName)


# rani = dpone_medical()
# print(rani.clgname)
# print(rani.dpname)
# print(rani.universityName)
