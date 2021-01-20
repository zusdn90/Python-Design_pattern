# 서비스 종류에 따라 알맞은 내용을 포함하는 프로필을 생성하는 프로그램
from abc import ABCMeta, abstractmethod

# 프로필의 각 세션을 나타낸다.
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")
        
class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicSection(Section):
    def describe(self):
        print("Public Section")                        

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()
    
    @abstractmethod
    def create_profile(self):
        pass       
    
    def get_sections(self):
        return self.sections
    
    def add_sections(self, section):
        self.sections.append(section)

class LinkedIn(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection)        
        self.add_sections(PatentSection)        
        self.add_sections(PublicSection)        

class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection)
        self.add_sections(AlbumSection)

if __name__ == '__main__':
    # Profile 추상 클래스에는 각 프로플에 들어갈 섹션에 대한 정보가 없다.
    # 예를 들어 페이스북 프로필에는 개인정보, 앨범 섹션이 있듯이 서브 클래스(Facebook)가 이를 결정한다.
        
    profile_type = input("Which Profile you'd like to create? [LinkedIn or Facebook]")        
    profile = eval(profile_type)()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.get_sections())
            