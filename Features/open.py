import os
import webbrowser

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ", "")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ", "")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif any(keyword in Query for keyword in ["open", "start"]):
        # Extract the name of the application or file
        Nameoftheapp = Query.split(maxsplit=1)[1]
        if os.name == 'nt':  # Windows OS
            os.startfile(Nameoftheapp)
        elif os.name == 'posix':  # macOS
            os.system(f"open '{Nameoftheapp}'")
        return True

    return False  # Return False if the query does not match any action
