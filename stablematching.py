
preferred_rankings_men = {
    'ryan': ['lizzy', 'sarah', 'zoey', 'danielle'],
    'josh': ['sarah', 'lizzy', 'danielle', 'zoey'],
    'blake': ['sarah', 'danielle', 'zoey', 'lizzy'],
    'conner': ['lizzy', 'sarah', 'zoey', 'danielle']

}

preferred_ranking_women = {
    'lizzy': ['ryan', 'blake', 'josh', 'conner'],
    'sarah': ['ryan', 'blake', 'conner', 'josh'],
    'zoey': ['conner', 'josh', 'ryan', 'blake'],
    'danielle': ['ryan', 'josh', 'conner', 'blake']
}

# Tentative pairings/keeps track of people that may end up together
tentative_pairings = []
# men who still need to propose and get accepted
free_men = []


def init_free_men():
    for man in preferred_rankings_men.keys():
        free_men.append(man)


def begin_matching(man):
    print("DEALING WITH %s" % (man))
    for woman in preferred_rankings_men[man]:
        taken_match = [couple for couple in tentative_pairings if woman in couple]

        if len(taken_match) == 0:  # if she isn't taken
            tentative_pairings.append([man, woman])
            free_men.remove(man)  # remove man that just got girl from list
            print('%s is no longer a free man and is now tentatively engaged to %s' % (man, woman))
            break

        elif len(taken_match) > 0:  # if she is taken, we compare the two guys
            print('%s is taken already...' % (woman))
            current_guy = preferred_ranking_women[woman].index(taken_match[0][0])
            potential_guy = preferred_ranking_women[woman].index(man)

            if current_guy < potential_guy:  # old guy better than new guy
                print("She\'s is happy with %s" % (taken_match[0][0]))
            else:  # new guy better than old guy
                print("%s is better than %s" % (man, taken_match[0][0]))
                print("Making %s free again...tentatively accept marriage between %s and %s" % (taken_match[0][0], man, woman))

                # new guy engaged
                free_men.remove(man)

                # old guy single now
                free_men.append(taken_match[0],[0])

                #  Update fiance (pass by reference trick which lets us compare next guy to guy that just got engaged)
                taken_match[0][0] = man
                break


def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)


def main():
    init_free_men()
    stable_matching()
    print('Complete list of marriage acceptances:  ')
    print(tentative_pairings)


main()
