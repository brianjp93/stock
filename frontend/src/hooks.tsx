import {  useQuery } from "react-query";
import * as api from "./api/api";

export function useUserQuery() {
  return useQuery("user", () => api.account.me(), {
    retry: false,
    refetchOnWindowFocus: false,
    staleTime: 1000 * 60 * 60,
    refetchOnMount: false,
  });
}
