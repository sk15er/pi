def generate_pi_digits(n):
    """Generate the first n digits of pi."""
    from mpmath import mp

    # Set the precision for mpmath
    mp.dps = n + 1  # extra digit for rounding
    pi_digits = str(mp.pi)[2:]  # get pi as a string and remove "3."
    
    return pi_digits[:n]  # return only the first n digits