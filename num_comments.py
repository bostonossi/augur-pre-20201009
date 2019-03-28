def num_comments(self):
    """collect the number comments in a pull request"""
    # obtain the data from GitHub's API
    comment_list = GET /repos/:owner/:repo/pulls/:number/commits
    num_comments = comment_list["comment_count"]
    return num_comments 
