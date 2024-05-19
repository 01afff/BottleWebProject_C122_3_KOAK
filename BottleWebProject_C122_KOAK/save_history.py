import json
from datetime import datetime


def createhistory(methodname, data):
    """
    ���������� ������� ���������� ���������� � ���� "calchistory.json".
    """

    try:
        # �������� ������� ���� "calchistory.json" ��� ������
        with open('calchistory.json', 'r') as read_json:
            # ��������� ������ �� ����� � ������� history
            history = json.load(read_json)
    except FileNotFoundError:
            # ���� ���� �� ������, ������� ����� ������� history � ������� �������� ��� ������� ���������    
            history = {}
            history["Prima"] = []
            history["Daykstra"] = []
            history["Floyda"] = []
            history["Kraskala"] = []
    except:
        # ���� �������� ����������� ������, ���������� ��������� �� ������
        return "Unknown error"
    
    # �������� ������� ���� � ����� � ������� "YYYY-MM-DD HH:MM:SS"
    current_day = datetime.now()
    string = current_day.strftime('%Y-%m-%d %H:%M:%S')
    
     # ��������� ������ � �������, � ����������� �� ����� ���������
    if(methodname == "Prima"):
        # ���� �������� �����, �� ��������� ������� ���� � �����, ������ ����� � ���
        history["Prima"].append({"date":string, "edge_list":data[0], "mst":data[1]})
    elif(methodname == "Kraskala"):
        # ���� �������� ��������, �� ��������� ������� ���� � �����, ������ ����� � ���
        history["Kraskala"].append({"date":string, "edge_list":data[0], "mst":data[1]})
    elif(methodname == "Floyda"):
        # ���� �������� ������, �� ��������� ������� ���� � �����, �������� ������� ��������� � �������������� �������
        history["Floyda"].append({"date":string, "original":data[0], "result":data[1]})
    elif(methodname == "Daykstra"):
        # ���� �������� ��������, �� ��������� ������� ���� � �����, �������� ������� ��������� � �������������� �������
        history["Daykstra"].append({"date":string, "original":data[0], "result":data[1]})
    
    # ���������� ����������� ������� history � ���� "calchistory.json"  
    with open('calchistory.json', 'w') as outfile:
        json.dump(history, outfile, indent = 3)
        

