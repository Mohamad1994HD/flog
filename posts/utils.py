def limit(qs, upto=None):
    min_length = upto
    qs_length = len(qs)

    if qs_length < min_length:
        min_length = qs_length

    return min_length

def slice_(qs, frm=None, to=None):
    upto = frm + to
    return qs[frm:limit(qs, upto)]        
