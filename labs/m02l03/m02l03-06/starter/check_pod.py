import json

pod = json.load(open("pod.json"))
pod_ctx = pod["spec"].get("securityContext", {})
for c in pod["spec"]["containers"]:
    ctx = c.get("securityContext", {})
    def get(key):  # a container's own setting overrides the pod's
        return ctx.get(key, pod_ctx.get(key))
    caps = ctx.get("capabilities", {})
    added = set(caps.get("add", []))
    seccomp = (get("seccompProfile") or {}).get("type")
    failed = [name for name, ok in [
        ("no privilege escalation", get("allowPrivilegeEscalation") is False),
        ("runAsNonRoot true", get("runAsNonRoot") is True),
        ("runAsUser not 0", get("runAsUser") != 0),
        ("drop ALL capabilities", "ALL" in caps.get("drop", [])),
        ("add only NET_BIND_SERVICE", added <= {"NET_BIND_SERVICE"}),
        ("seccomp profile set", seccomp in ("RuntimeDefault", "Localhost")),
    ] if not ok]
    print(c["name"], "violates restricted" if failed else "meets restricted")
    for name in failed:
        print("  needs", name)
