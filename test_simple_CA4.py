import unittest
from process_changes_CA4 import get_commits, read_file, get_authors, get_dates, get_lines

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')
        
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('Jimmy', commits[420]['author'])
        self.assertEqual(['FTRPC-500: Frontier Android || Inconsistencey in My Activity screen',
				'Client used systemAttribute name="Creation-Date" instead of versionCreated as version created.'],
				commits[24]['comment'])
        self.assertEqual(['M /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/model/src/com/biscay/client/android/model/util/sync/dv/SyncAdapter.java'],
                commits[20]['changed_path'])
                
    def test_number_of_commit_authors(self):
        commits = get_commits(self.data)
        authors = get_authors(commits)
        self.assertEqual(152, authors['Jimmy'])
    
    def test_of_dates(self):
        commits = get_commits(self.data)
        dates = get_dates(commits)        
        self.assertEqual(3, dates['2015-11-17'])

    def test_of_lines(self):
        commits = get_commits(self.data)
        lines = get_lines(commits)        
        self.assertEqual(348, lines[1])
                
        
if __name__ == '__main__':
    unittest.main()
