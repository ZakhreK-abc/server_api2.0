from fastapi import APIRouter
import requests


router = APIRouter(prefix="/dashboard", tags=["proxmox"])

@router.get("/vm-stat/{vm_id}")
def get_vm_status(vm_id: int):
    print("a")
    url = f"https://192.168.0.103:8006/api2/json/nodes/pve/qemu/{vm_id}/status/current"
    headers={"Authorization": "PVEAPIToken=root@pam!api-monitor=f641a86b-19fb-43ec-8c84-dc6ac098beac"}
    response = requests.get(url, headers=headers, verify=False)
    
    return response.json()


@router.post("/shutdown-server")
def shutdown_server():
    response = requests.post(
    "https://192.168.0.103:8006/api2/json/nodes/pve/status",
    headers={"Authorization": "PVEAPIToken=root@pam!api-monitor=f641a86b-19fb-43ec-8c84-dc6ac098beac"},
    json={"command": "shutdown"},
    verify=False
    )

    return response

@router.get("/shutdown-vm/{vm_id}")
def shutdown_vm(vm_id: int):
    url = f"https://192.168.0.103:8006/api2/json/nodes/pve/qemu/{vm_id}/status/shutdown"
    headers = {"Authorization": "PVEAPIToken=root@pam!api-monitor=f641a86b-19fb-43ec-8c84-dc6ac098beac"}
    
    response = requests.post(url, headers=headers, verify=False)
    return response.json()