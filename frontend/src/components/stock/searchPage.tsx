import { useState } from "react";
import { useQuery } from 'react-query';
import Form from "react-bootstrap/Form";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col'

import { Skeleton } from "../general/skeleton";
import * as api from "../../api/api";

export function SearchPage() {
  return (
    <Skeleton>
      <Search />
    </Skeleton>
  );
}

export function Search() {
  const [searchText, setSearchText] = useState("");
  const [search, setSearch] = useState("");

  const searchQuery = useQuery(
    ['stock-search', searchText],
    () => api.stock.search(searchText),
    {retry: false, refetchOnWindowFocus: false}
  )

  return (
    <>
    <Form>
      <Form.Group>
        <Form.Label>Search</Form.Label>
        <Form.Control
          value={search}
          onChange={(event) => setSearch(event.target.value)}
          type="text"
          placeholder="Search"
        />
      </Form.Group>
    </Form>
    {searchQuery.isSuccess && searchQuery.data.map(item => {
        return (
          <Row>
            <Col>{item}</Col>
          </Row>
        )
      })
    }
    </>
  );
}
