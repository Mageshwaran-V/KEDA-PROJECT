import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 50,
  duration: '30s',
};

export default function () {
//http.get('http://dot.74.225.18.84.nip.io');
http.get('http://dot.74.225.12.9.nip.io');
  sleep(1);
}
