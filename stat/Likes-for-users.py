import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import json
import datetime


def main():
    """Usage: likes-for-users.py filename.json

Assumes filename.json is a JSON GroupMe transcript.
    """

    if len(sys.argv) < 2:
        print(main.__doc__)
        sys.exit(1)

    transcriptFile = open(sys.argv[1])
    transcript = json.load(transcriptFile)
    transcriptFile.close()

    names = {}
    counts = {}
    likes = {}
    mlikes = {}
    totallikes = 0
    mtotallikes = 0

    for message in transcript:
        name = message[u'name']
        id = message[u'user_id']
        like = len(message[u'favorited_by'])
        mlike = 0
        if len(message[u'favorited_by']) is not 0:
            mlike = 1

        names[id] = name

        if id not in counts:
            counts[id] = 0
        else:
            counts[id] = counts[id] + 1

        if id not in likes:
            likes[id] = 0
        else:
            likes[id] = likes[id] + like

        if id not in mlikes:
            mlikes[id] = 0
        else:
            mlikes[id] = mlikes[id] + mlike

        totallikes = totallikes + like
        mtotallikes = mtotallikes + mlike

    totalMessages = len(transcript)
    print('total message count: ' + str(totalMessages))
    print('total liked: ' + str(totallikes))
    print('total messages like: ' + str(mtotallikes))

    for id, count in counts.items():
        name = names[id]
        percentageL = round(likes[id]/float(totallikes) * 100)
        hitpercentage = round(mlikes[id]/float(count) * 100)
        print(name + ': Likes: ' + str(likes[id]) + ' (' + str(percentageL) + '%) Post Liked: ' +str(mlikes[id]) + '  HIT%: ' + str(hitpercentage) + '%')


if __name__ == '__main__':
    main()
    sys.exit(0)
