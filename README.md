This role is a sample of ansible.
Please use this a training, hands-on and etc.

Usage:

```yaml
- import_role:
    name: irixjp.role_example_hello
```

```
TASK [debug] *******************************
ok: [localhost] => {
    "msg": "Hello"
}
```

This role has a custom module `sample_get_locale`. The module returns OS locale setting.

```yaml
---
- import_role:
    name: irixjp.role_example_hello

- name: get locale
  sample_get_locale:
  register: ret

- debug: var=ret
```

```
TASK [irixjp.role_example_hello : say hello! (en_US.UTF-8)] ****
ok: [node-1] => {
    "msg": "Hello"
}

TASK [get locale] **********************************************
ok: [node-1]

TASK [debug] ***************************************************
ok: [node-1] => {
    "ret": {
        "changed": false,
        "failed": false,
        "locale": "en_US.UTF-8"
    }
}
```
