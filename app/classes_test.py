import unittest
from models import Sources,Articles
# Sources = sources.Sources
# Articles=sources.Articles

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

    def test_init(self):
        '''
        test_init to ensure objects are instantiated correctly
        :return:
        '''
        self.assertEqual(self.new_source.id, "cnn")
        self.assertEqual(self.new_source.name, "cnn")
        self.assertEqual(self.new_source.description, "news from around the world")
        self.assertEqual(self.new_source.language, "en")


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('mark',"bitcoin review",'bitcoin news from relevant authorities',"en","2018-09-01T06:27:00Z","http://foxnews.com/img345.jpg")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_init(self):
        '''
        test_init to ensure objects are instantiated correctly
        :return:
        '''
        self.assertEqual(self.new_article.author, "mark")
        self.assertEqual(self.new_article.title, "bitcoin review")
        self.assertEqual(self.new_article.description, "bitcoin news from relevant authorities")
        self.assertEqual(self.new_article.url, "en")
        self.assertEqual(self.new_article.publishedAt, "2018-09-01T06:27:00Z")
        self.assertEqual(self.new_article.urlToImage, "http://foxnews.com/img345.jpg")



# class Articles:
#     def __init__(self,author,title,description,url,publishedAt,urlToImage):
#         self.author=author
#         self.title=title
#         self.description=description
#         self.url=url
#         self.publishedAt=publishedAt
#         self.urlToImage=urlToImage


if __name__ == '__main__':
    unittest.main()


    # def __init__(self,id,name,description,language):
    #     self.id=id
    #     self.name=name
    #     self.description=description
    #     self.language=language