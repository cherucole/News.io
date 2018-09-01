import unittest
from models import sources
Sources = sources.Sources
Articles=sources.Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('cnn',"cnn",'news from around the world',"en")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()


    # def __init__(self,id,name,description,language):
    #     self.id=id
    #     self.name=name
    #     self.description=description
    #     self.language=language