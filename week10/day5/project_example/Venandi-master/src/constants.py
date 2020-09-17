import pandas as pd

#users countries source --> it is better to select 1 by 1 or small groups, as this big group can take almost a day and the risk
#to have a 403 error is higher, however with a range of 1-3 countries should work although it can take the whole night :D 
#btw, the countries are the top 25 best programmers countries by hackerrank
"""countries = ["china", "russia", "poland", "switzerland", "hungary", "japan", "taiwan", "france", "czech", "italy", "ukraine", "bulgaria", "singapore",
 "germany", "finland", "belgium", "hong kong", "spain", "australia", "romania", "canada", "vietnam", "usa", "uk", "india"]"""
countries = ["taiwan"]

#ranges of followers to request
followers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13..14", "15..17", "18..20", "21..25", "26..35", "36..50", "51..99", ">100"]

#we use it to request github api with the parameters given from flask
seniority_dict = {
    "followers": {
        "junior":"0..7",
        "middle":"8..25",
        "senior":"26..70",
        "principal":"71..250",
        "architect":">250"
    },
    "repos": {
        "junior":"0..12",
        "middle":"12..40",
        "senior":">70",
        "principal":">20",
        "architect":">25" 
    }
}

#we use it to show the predicted sionirity of the requested user
labels_dict= {
    0:"junior",
    1:"middle",
    2:"senior",
    3:"principal",
    4:"architect"
}

