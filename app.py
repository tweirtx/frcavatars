from flask import Flask, request, send_from_directory
import base64
import os

app = Flask(__name__)


@app.route('/get_image')
def get_image():
    team = request.args.get('team')
    files = os.listdir('avatars')
    if '{}.png'.format(team) not in files:
        img_data = b'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAAARnQU1' \
                   b'BAACxjwv8YQUAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAJP0lEQVRYR62Y63NVVxnG+Xuc' \
                   b'qh+csTM6o7VDLdK0Y5G2WHphmKlWwcFJlYnQCdoCkVsFoVgusUykSLklXCxIKIIkJWlCTpKWgJAGQpmCLSlJgJzknH328v0' \
                   b'96+ydc0520gB+ePd9v+tZ7/VZa4pzLlHC3Gd2iq6vxNe6D3qK7mMJB+2U8Pw+xF+EN+3kpuRGjrhc5pQDUG6kzuWGt7tgaKML0lt' \
                   b'dcGeFC7OtzoV99u49e7dD90F6k50/1DPp+j+LvwiHbOC0gfmzAXxf4DIDM9zIlw+47OBcO3/DZW9XGsilLnur3GX6p7uRvm/pm+' \
                   b'yt+fbfBg9akzPLh7dN7djB7kXsEMRWA0Bw5w8G6GseAEDsOjs4R+fMzQf9Oz17Ib7O3PyOrJzLNMnCXnmQP9+f6JDLfOD' \
                   b'C4ILA9X5S6cqW17qZf9znZq/e655dudvNWrnHPVm1zz1hzyXL9ul++tI69/N1f3d9Vx7RhJhgmG02lcmD3YvoQCwRb9nB2a734nz' \
                   b'3IxsYAUAkjy0blcdNyvLCdwve3OEt2V+mEHEuY5a0hAmH7Tp54MmKDmHuhlxEzH168SkDVOtmrzrkzp7tdO0dHePKh2dS+Q' \
                   b'nUugtd8xQCmYFZ5o3zpjZ5wLsVHXIj9ZYEFSYL3eX/zHLTXq91L619z7W1t7vW1Phyxt7XHWuWFQmDnvPP+vi0hEJnmO0w' \
                   b'K1oClgx6N+IvKB0Wh5mBH7ventfcNBtwMgB539Sack8u3y+QG/YQJnPiaoBuX0Ozur4X0YEszt4yF/U/bBZ8RgDnvvEPdyYBVK' \
                   b'G0tHmQkatJnvbUb1SaqI/B0FpTbwPdhxXt5347uynMWhbsXiBrYMGPPup0KQMACASXloKOQC7eckz/La3ZaQBfki4KvwbKN4J7E' \
                   b'X9hM8wN71LRxYIMRLb+pOqAlZsD7pkVB9xPVx50z68+JGsBDFCFQHmOqx+zhGk5s1ixSNnC1WHQZcOMHXwyogO9NbhTpQzsv' \
                   b'eAB4uapr9W6R16vkzxqiUPyALyxua0IHIJl/7L73/qXWtl1dpFqI+DoMuP2768QHXIjB5VxxE76i++5q90z3KfdM93VnnJ/vrRI' \
                   b'54Vv/U0AqIMtbd6SRSDNqsQu32yrW20xPU1xSPjQr2kGtNRCAF8l8YXanXUBgpuCnRmYaecXVH5oeZn+H7rB61PdL9btEABcX' \
                   b'+pmhPrIBPim+9zz9t9Us6AZwMABMhpvshJf5DKNpqDVFF1S3ORGDvm4NJC43/fchxQGtDkAJAHk2atbjur9kupqXxfR' \
                   b'YY0gGutusjp/4esUbvbuNqD5nprLnFBGeoAPup5zs1VOSKAkgAhWxMKAbDj9qv2LqzeqnWqc3HWdJyOJD5Ew97msSU8FNNS' \
                   b'KdgaJYOCkGCyU6toGfTfNEmy47+sKE3nGQql0LC/J7GfMg0KBFwbpt6z8vGzW+76ShGwmESYCyLtCV694pyb2QJCu0aTD' \
                   b'bJu4I14TEWbMhHpZdFMoWFAk1pg0yk83l5tb98q1FO8kYKXS2dkRMx7PL83V8EYrO0F6m4ACWFYtWi6MWjMGVChyr+LRFG' \
                   b'vmo9Y7crIlEcx4UnOwUQDhjdJl8ZwZeFqtlcYgmnf7ldG2WCJjHiAU12BojeIGpadO/1YdgvbHoNS7CACtjntcmlgbTYhDQ' \
                   b'K5/d53pLFNWo7ez/WUlHYwcJkU4yeVaNvgWXAxOJLNfycHssNzJps1KDLoIHaS0F3dYxgLsVJN/lwTyeGOrJoi7SRjA/a' \
                   b'uhQuUKmnax60V79oCsGQbdAhZJAbi0veyxeGhU3PExM9u8Z63ALa85rsEKrQc4ejC9mm/qT7XqWfQ+Ev6JXM0SgnABM' \
                   b'PcIIOEAGATDjK5rCgB6sw7JtZF7TzRWSgFEoXRQXNrUknK/XH84dmFldf24AJnI43neiDAhShG6uQf4tV5I82LVTFxdBN' \
                   b'CFXyrdKSn0ZFyxavtGkYY9R5sTBwUgRALKv27nm6584z9dxeZ6ZXlpKPD9MbPwD4yALN5aHxd5Mj1qjec+nqtMR+hiFPS8' \
                   b'9a6Ye411GKsG/dAXT7vDx5dolliocCANZkKsUXLoKjDp5pZFYjGsZXBnKsGS+rcEPF2H8JFVTc53/dqy/AmrI' \
                   b'CwZWr1r6RSqSbZshBRcODtHJaXMfoiCv2gQk/cbWqWU2kiPzg4+5/Yf+1O8XCj8fiKJCO+CDUdikCRRbnivrGj9t02+1qIJJm' \
                   b'xlgHLAx1jCKynOTKwDL8S1zS2vqK6RhVw/t2q3q9h0VFaJ3DieoJdvYO5MSgAtZATQjEYdlou1yLGbO59/2+0+XKW4gj1Hr' \
                   b'ixUyrNdR04rC3+1/h0lE9mHUiTqOFhEZWkCkMQq8R0tuiDIK7dvjdkPFUUAaTXQKAbwQV8nF5YqBGyH2pdXOHitTP8QFmQ' \
                   b'fPBJLbnh3vQIfS0ZLhFEdPg5Zc6/deVJ6CKel2za5t2vXeH1W3tTJhnf47I1aGplIDGA9FFAyyDKEa8BFAV29/22vzAI6zH' \
                   b'5s8btEAGE9HZ3LZF0KM8uAKIYBh9WI6xfXHJIeDAKZSPf9TPqoIp6P1vkkAWCQ/qtSmx8Q4oviWyjUq6hmMQlfDqYbMFsYqSRY' \
                   b'/85dlXuwwOWL8/yejrmPTgJAMhbPRGUFdn6iscI88V3FMaCkz8gynqVxmIszsXsjgACIFkqlwvuG5jfc8I1vGpg5mq0vUZy7Zcmo' \
                   b'h7NnQ6liwizwoWmEDzoWbtnlblyZYTp87eM/UTH2dQTOuKidRfVpbbAMtj0udy/SmR0GySeV7pJZg20NrBJtb4gmmeVEm0wRFE' \
                   b'nLBVsLU0tZ01zr/b1YDIAAyZlamUr9zu+IKURs/cx6KL+LO9qLPVAlCUSRTM7eWmBSroWSyIIteCK6j1CGEGqUB7jXFN/IK/S' \
                   b'z1gBGONDHP/1XH4rXMGRo/3WzmDaZZphhqgzcidH/8yALJTYlohhQen+gOPAxUWVg58kybFACSt+Hwwamx888Wkqys0rSsQAz' \
                   b'oGwiaXJGVgf+O1/X2iQ1q/txCAuWojBpSOpY2h9fRGsFFUhMzsIp32VEg6Dn+cl4th3R87EbQ5GbxJwNEECISyaMhzyli3YbJt' \
                   b'6JLbhhoGjj0ZNFgShaJyTPckKRpVl8eaakMChypY+18STx4f0Lk7Wk0cqwOOixnDxQ9P144qb8DwUO3JE5R0eiAAAAAElFTkSuQmCC'
        # Get this automatically from TBA
        with open("avatars/{}.png".format(team), "w") as fh:
            fh.write(base64.decodebytes(img_data))
    return '/avatars/{}.png'.format(team)


@app.route('/avatars/<path:path>')
def avatars(path):
    return send_from_directory('avatars', path)


app.run(port=80)
