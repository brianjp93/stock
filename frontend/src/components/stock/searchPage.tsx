import { useState } from "react";
import { useQuery } from 'react-query';
import Form from "react-bootstrap/Form";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'

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
    ['stock-search', search],
    () => api.stock.search(search).then(response => response.result),
    {retry: false, refetchOnWindowFocus: false}
  )

  return (
    <>
    <Form onSubmit={() => {}}>
      <Form.Group>
        <Form.Label>Search</Form.Label>
        <Form.Control
          value={searchText}
          onChange={(event) => setSearchText(event.target.value)}
          type="text"
          placeholder="Search"
        />
        <Button type='button' onClick={() => setSearch(searchText)}>Search</Button>
      </Form.Group>
    </Form>
    {searchQuery.isSuccess && searchQuery.data.map(item => {
      return (
        <Row>
          <Col>{item.symbol}</Col>
          <Col>{item.description}</Col>
          <Col>{item.displaySymbol}</Col>
          <Col>{item.type}</Col>
        </Row>
      )
    })}
    </>
  );
}
