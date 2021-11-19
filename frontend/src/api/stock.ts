import axios from "axios";

const base = "/api/stock";

export async function search(q: string) {
  const url = `${base}/search/`;
  const response = await axios.get(url, { params: { q } });
  return response.data;
}

export async function basicFinancials(code: string) {
  const url = `${base}/basic/${code}/`
  const response = await axios.get(url)
  return response.data
}
