from exceptions import UploadError

import ubinascii
import uos
import urequests


def make_request(data, image=None):
    boundary = ubinascii.hexlify(uos.urandom(16)).decode('ascii')

    def encode_field(field_name):
        return (
            b'--%s' % boundary,
            b'Content-Disposition: form-data; name="%s"' % field_name,
            b'', 
            b'%s'% data[field_name]
        )

    def encode_file(field_name):
        filename = 'latest.jpeg'
        return (
            b'--%s' % boundary,
            b'Content-Disposition: form-data; name="%s"; filename="%s"' % (
                field_name, filename),
            b'', 
            image
        )

    lines = []
    for name in data:
        lines.extend(encode_field(name))
    if image:
        lines.extend(encode_file('file'))
    lines.extend((b'--%s--' % boundary, b''))
    body = b'\r\n'.join(lines)

    headers = {
        'content-type': 'multipart/form-data; boundary=' + boundary,
        'content-length': str(len(body))}
    return body, headers


def upload_image(url, headers, data):
    http_response = urequests.post(
        url,
        headers=headers,
        data=data
    )
    if http_response.status_code == 204:
        print('Uploaded request')
    else:
        raise UploadError(http_response)
    http_response.close()
    return http_response
