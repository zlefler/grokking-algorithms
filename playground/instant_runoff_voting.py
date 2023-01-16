def runoff(voters):
    def check_first_place(voters):
        first_choices = {}
        for vote in voters:
            if vote[0] in first_choices:
                first_choices[vote[0]] += 1
            else:
                first_choices[vote[0]] = 1
        for candidate, votes in first_choices.items():
            if votes > len(voters) * .5:
                return candidate
            else:
                new_list = remove_last_place(first_choices, voters)
                if new_list:
                    check_first_place(new_list)
                else:
                    return None

    def remove_last_place(first_choices, voters):
        losers = []
        lowest_vote_count = float('inf')
        for candidate, votes in first_choices.items():
            if votes < lowest_vote_count:
                lowest_vote_count = votes
                losers = [candidate]
            elif votes == lowest_vote_count:
                losers.append(candidate)
        if len(losers) == total:
            return None
        for candidate in losers:
            for voter in voters:
                if candidate == voter[0]:
                    voter.remove(candidate)
        check_first_place(voters)

    total = len(voters[0])
    return check_first_place(voters)


voters = [["dem", "ind", "rep"],
          ["rep", "ind", "dem"],
          ["ind", "dem", "rep"],
          ["ind", "rep", "dem"]]

print(runoff(voters))
